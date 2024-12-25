from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import io
from PIL import Image
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import math

# 初始化 Flask 应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 初始化文本检测和识别模型
ocr_detection = pipeline(
    Tasks.ocr_detection, model="damo/cv_proxylessnas_ocr-detection-db-line-level_damo"
)
ocr_recognition = pipeline(
    Tasks.ocr_recognition, model="damo/cv_convnextTiny_ocr-recognition-general_damo"
)


def crop_image(img, position):
    """裁剪图像到指定的矩形区域"""

    def distance(x1, y1, x2, y2):
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

    position = position.tolist()
    for i in range(4):
        for j in range(i + 1, 4):
            if position[i][0] > position[j][0]:
                tmp = position[j]
                position[j] = position[i]
                position[i] = tmp
    if position[0][1] > position[1][1]:
        tmp = position[0]
        position[0] = position[1]
        position[1] = tmp

    if position[2][1] > position[3][1]:
        tmp = position[2]
        position[2] = position[3]
        position[3] = tmp

    x1, y1 = position[0][0], position[0][1]
    x2, y2 = position[2][0], position[2][1]
    x3, y3 = position[3][0], position[3][1]
    x4, y4 = position[1][0], position[1][1]

    corners = np.zeros((4, 2), np.float32)
    corners[0] = [x1, y1]
    corners[1] = [x2, y2]
    corners[2] = [x4, y4]
    corners[3] = [x3, y3]

    img_width = distance((x1 + x4) / 2, (y1 + y4) / 2, (x2 + x3) / 2, (y2 + y3) / 2)
    img_height = distance((x1 + x2) / 2, (y1 + y2) / 2, (x4 + x3) / 2, (y4 + y3) / 2)

    corners_trans = np.zeros((4, 2), np.float32)
    corners_trans[0] = [0, 0]
    corners_trans[1] = [img_width - 1, 0]
    corners_trans[2] = [0, img_height - 1]
    corners_trans[3] = [img_width - 1, img_height - 1]

    transform = cv2.getPerspectiveTransform(corners, corners_trans)
    dst = cv2.warpPerspective(img, transform, (int(img_width), int(img_height)))
    return dst


def order_point(coor):
    """对点进行排序，确保以顺时针顺序排列"""
    arr = np.array(coor).reshape([4, 2])
    sum_ = np.sum(arr, 0)
    centroid = sum_ / arr.shape[0]
    theta = np.arctan2(arr[:, 1] - centroid[1], arr[:, 0] - centroid[0])
    sort_points = arr[np.argsort(theta)]
    sort_points = sort_points.reshape([4, -1])
    if sort_points[0][0] > centroid[0]:
        sort_points = np.concatenate([sort_points[3:], sort_points[:3]])
    sort_points = sort_points.reshape([4, 2]).astype("float32")
    return sort_points


def draw_detected_boxes(image_full, det_result):
    """在图像上绘制检测到的文本框"""
    image_with_boxes = image_full.copy()
    for box in det_result:
        points = np.array(box, dtype=np.int32).reshape((-1, 2))
        cv2.polylines(
            image_with_boxes, [points], isClosed=True, color=(0, 255, 0), thickness=2
        )
    image_with_boxes_rgb = cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_with_boxes_rgb)
    buffered = io.BytesIO()
    pil_image.save(buffered, format="PNG")
    buffered.seek(0)
    base64_image = base64.b64encode(buffered.read()).decode("utf-8")
    return base64_image


@app.route("/process_image", methods=["POST"])
def process_image():
    """处理上传的图像并返回检测和识别结果"""
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image file provided."}), 400

        file = request.files["image"]
        np_img = np.frombuffer(file.read(), np.uint8)
        image_full = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        det_result = ocr_detection(image_full)
        det_result = det_result["polygons"]

        results = []
        for i in range(det_result.shape[0]):
            pts = order_point(det_result[i])
            image_crop = crop_image(image_full, pts)
            recognition_result = ocr_recognition(image_crop)
            results.append({"box": pts.tolist(), "text": recognition_result["text"]})

        base64_image = draw_detected_boxes(image_full, det_result)

        return jsonify({"image": base64_image, "detections": results})

    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
