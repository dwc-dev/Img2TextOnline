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
        <ImageUpload @upload-success="handleUploadSuccess" />
        <div class="upload-instructions">
          <p>支持 jpg/png 文件，且不超过 10MB</p>
        </div>
      </el-card>

      <!-- 图像可视化效果区域 -->
      <el-card class="visualization-card">
        <template #header>
          <div class="card-header">
            <span>图像可视化效果</span>
          </div>
        </template>
        <img v-if="imageUrl" :src="imageUrl" alt="Uploaded Image" class="uploaded-image" />
        <p v-else>请上传图片以查看效果。</p> <!-- 提示信息 -->
      </el-card>
    </div>

    <!-- 一键识别按钮 -->
    <div class="button-container">
      <el-button type="primary" @click="oneClickIdentify" class="identify-button">一键识别</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ImageUpload from '@/components/ImageUpload.vue'

const imageUrl = ref('')

const handleUploadSuccess = (data: { url: string }) => {
  imageUrl.value = data.url // 确保 URL 被正确设置
}

// 一键识别的处理函数
const oneClickIdentify = () => {
  // 处理一键识别的逻辑
}
</script>

<style scoped>
.home-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.content-container {
  display: flex; /* 使用 flexbox 布局 */
  justify-content: space-between; /* 左右对齐 */
}

.upload-card, .visualization-card {
  width: 48%; /* 设置宽度 */
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
  color: #888; /* 修改说明文字颜色 */
}

.button-container {
  display: flex;
  justify-content: center; /* 居中按钮 */
  margin-top: 20px; /* 添加顶部间距 */
}

.uploaded-image {
  max-width: 100%; /* 确保图像适应容器 */
  height: auto; /* 保持图像比例 */
}
</style> 