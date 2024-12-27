# Img2TextOnline (Backend)

这是 Img2TextOnline 项目的后端部分，使用 Python Flask 和 modelscope 实现。

## 项目说明

文本检测模型：
[读光-文字检测-轻量化端侧DBNet行检测模型-中英-通用领域](https://www.modelscope.cn/models/iic/cv_proxylessnas_ocr-detection-db-line-level_damo/summary)

文本识别模型：
[读光-文字识别-行识别模型-中英-通用领域](https://modelscope.cn/models/iic/cv_convnextTiny_ocr-recognition-general_damo)

实现的API：
返回图片中检测到的文字框坐标、对应的文字内容，以及绘制了文字框的处理后的图片的 Base64 编码

注：本项目中部分代码参考自[https://modelscope.cn/headlines/article/42](https://modelscope.cn/headlines/article/42)

## Docker启动
```bash
docker-compose up
```

## API 说明

### 接口信息
```
类型：POST
地址：http://<server-ip>:8000/api/process_image
```

### 功能描述
该接口接收一张图片，通过 OCR 检测和识别处理，返回图片中检测到的文字框坐标、对应的文字内容，以及绘制了文字框的处理后的图片的 Base64 编码。

---

### 请求格式

#### Header
```
Content-Type: multipart/form-data
```

#### 请求体
| 参数名  | 类型                          | 必须 | 说明           |
| ------- | ----------------------------- | ---- | -------------- |
| `image` | 文件 (jpeg/png等图片格式文件) | 是   | 上传的图片文件 |

---

### 响应格式

#### 成功响应
HTTP 状态码：`200 OK`

##### 响应体
```json
{
  "image": "<Base64编码的图片>",
  "detections": [
    {
      "box": [[x1, y1], [x2, y2], [x3, y3], [x4, y4]],
      "text": "识别出的文字内容"
    },
    ...
  ]
}
```

##### 字段说明
| 字段名       | 类型     | 说明                                 |
| ------------ | -------- | ------------------------------------ |
| `image`      | `string` | 包含文字框的图片，Base64 编码        |
| `detections` | `array`  | 每个检测框的坐标及其对应的文字内容   |
| `box`        | `array`  | 四边形框的顶点坐标，按顺时针顺序排列 |
| `text`       | `string` | 框内识别出的文字                     |

#### 示例响应
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...",
  "detections": [
    {
      "box": [[26, 737], [779, 737], [779, 782], [26, 782]],
      "text": "Example Text 1"
    },
    {
      "box": [[192, 374], [597, 371], [598, 418], [193, 422]],
      "text": "Example Text 2"
    }
  ]
}
```

---

### 错误响应

#### 错误格式
HTTP 状态码：`400` 或 `500`

#### 错误响应示例
```json
{
  "error": "No image file provided."
}
```

#### 错误类型
| 状态码 | 错误信息                  | 说明                           |
| ------ | ------------------------- | ------------------------------ |
| `400`  | `No image file provided.` | 未提供图片文件                 |
| `500`  | `Internal Server Error`   | 服务器内部错误，可能是模型异常 |
