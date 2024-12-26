<template>
  <div class="home-page">
    <!-- 页面标题 -->
    <h1>Img2TextOnline - 在线图片转文字</h1>
    <div class="content-container">
      <!-- 图片上传区域 -->
      <el-card class="upload-card">
        <template #header>
          <div class="card-header">
            <span>图片上传</span>
          </div>
        </template>
        <!-- 图片上传组件 -->
        <ImageUpload
          :loading="isLoading"
          @upload-success="handleUploadSuccess"
        />
        <div class="upload-instructions">
          <p>支持图片文件</p>
        </div>
        <!-- 显示上传的图片 -->
        <div v-if="imageUrl" class="uploaded-image-container">
          <img :src="imageUrl" alt="Uploaded Image" class="uploaded-image" />
        </div>
      </el-card>

      <!-- 处理后图片区域 -->
      <el-card class="visualization-card">
        <template #header>
          <div class="card-header">
            <span>处理后图片</span>
          </div>
        </template>
        <div v-if="detectionResult">
          <img
            :src="'data:image/png;base64,' + detectionResult.image"
            alt="Processed Image"
            class="processed-image"
          />
        </div>
        <p v-else>请上传图片并进行识别以查看处理后的效果。</p>
        <!-- 提示信息 -->
      </el-card>
    </div>

    <!-- 一键识别按钮 -->
    <div class="button-container">
      <el-button
        type="primary"
        @click="oneClickIdentify"
        class="identify-button full-width"
        :loading="isLoading"
        >一键识别</el-button
      >
    </div>

    <!-- 检测结果展示 -->
    <div v-if="detectionResult" class="result-container">
      <h3>检测框及文字识别结果:</h3>
      <el-table :data="detectionResult.detections" stripe>
        <el-table-column label="框编号">
          <template #default="{ $index }">
            {{ $index + 1 }}
            <!-- 直接使用 $index 显示框编号 -->
          </template>
        </el-table-column>
        <el-table-column prop="box" label="框坐标" :formatter="formatBox" />
        <el-table-column prop="text" label="识别结果" />
      </el-table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import ImageUpload from "@/components/ImageUpload.vue";

const isLoading = ref(false); // 控制 loading 状态

// 定义检测结果的类型
interface Detection {
  box: number[]; // 检测框坐标
  text: string; // 识别的文本
}

interface DetectionResult {
  image: string; // 处理后的图片的 Base64 字符串
  detections: Detection[]; // 检测结果数组
}

// 响应式变量，存储上传的图片 URL 和检测结果
const imageUrl = ref("");
const detectionResult = ref<DetectionResult | null>(null); // 设置类型

// 处理上传成功的回调
const handleUploadSuccess = (data: { url: string }) => {
  imageUrl.value = data.url; // 确保 URL 被正确设置
};

// 一键识别的处理函数
const oneClickIdentify = async () => {
  if (!imageUrl.value) {
    alert("请先上传图片！"); // 提示用户上传图片
    return;
  }

  isLoading.value = true; // 开始加载

  const formData = new FormData();
  const response = await fetch(imageUrl.value); // 获取上传的图片
  const blob = await response.blob(); // 将图片转换为 Blob
  formData.append("image", blob, "uploaded_image.png"); // 将 Blob 添加到 FormData

  try {
    const result = await fetch("http://localhost:8000/process_image", {
      method: "POST",
      body: formData, // 发送图片到后端进行处理
    });

    if (!result.ok) {
      throw new Error("HTTP error " + result.status); // 处理错误
    }

    detectionResult.value = await result.json(); // 设置检测结果
  } catch (error) {
    console.error("识别失败:", error);
    alert("识别失败，请重试。"); // 提示用户识别失败
  } finally {
    isLoading.value = false; // 停止加载
  }
};

// 格式化框坐标
const formatBox = (row: Detection) => {
  return JSON.stringify(row.box); // 返回框坐标的字符串形式
};
</script>

<style scoped>
.home-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.content-container {
  display: flex;
  /* 使用 flexbox 布局 */
  justify-content: space-between;
  /* 左右对齐 */
}

.upload-card,
.visualization-card {
  width: 48%;
  /* 设置宽度 */
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.upload-instructions {
  margin-top: 10px;
  font-size: 14px;
  color: #888;
  /* 修改说明文字颜色 */
}

.uploaded-image-container {
  margin-top: 10px;
  /* 添加顶部间距 */
}

.uploaded-image {
  max-width: 100%;
  /* 确保图像适应容器 */
  height: auto;
  /* 保持图像比例 */
}

.button-container {
  margin-top: 20px;
  /* 添加顶部间距 */
}

.full-width {
  width: 100%;
  /* 按钮宽度设置为100% */
}

.result-container {
  margin-top: 20px;
}

.processed-image {
  max-width: 100%;
  /* 确保处理后的图像适应容器 */
  height: auto;
  /* 保持图像比例 */
}
</style>
