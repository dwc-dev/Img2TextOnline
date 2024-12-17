<template>
  <div class="home-page">
    <!-- 页面标题 -->
    <h1>Img2TextOnline - 在线图片转文字</h1>
    <!-- 图片上传区域 -->
    <el-card class="upload-card">
      <template #header>
        <div class="card-header">
          <span>图片上传</span>
        </div>
      </template>
      <!-- 图片上传组件 -->
      <ImageUpload @upload-success="handleUploadSuccess" />
    </el-card>

    <!-- 检测结果展示区域 -->
    <el-card v-if="detectionResult" class="result-card">
      <template #header>
        <div class="card-header">
          <span>检测结果</span>
        </div>
      </template>
      <!-- 检测结果组件 -->
      <DetectionResult 
        :image-url="imageUrl" 
        :result="detectionResult" 
      />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ImageUpload from '@/components/ImageUpload.vue'
import DetectionResultComponent from '@/components/DetectionResult.vue'

const imageUrl = ref('')
const detectionResult = ref(null)

const handleUploadSuccess = (data: any) => {
  imageUrl.value = data.url
  detectionResult.value = data.result
}
</script>

<style scoped>
.home-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.upload-card, .result-card {
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style> 