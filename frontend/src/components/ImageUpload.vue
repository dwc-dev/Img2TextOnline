<template>
  <!-- 图片上传组件 -->
  <el-upload
    class="upload-demo"
    drag
    action="/api/upload"
    :on-success="handleSuccess"
    :on-error="handleError"
    :before-upload="beforeUpload"
    accept=".jpg,.jpeg,.png"
  >
    <!-- 上传图标 -->
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <!-- 提示文本 -->
    <div class="el-upload__text">
      拖拽文件到此处或 <em>点击上传</em>
    </div>
    <!-- 补充说明 -->
    <template #tip>
      <div class="el-upload__tip">
        支持 jpg/png 文件，且不超过 10MB
      </div>
    </template>
  </el-upload>
</template>

<script setup lang="ts">
// 导入所需的依赖
import { defineEmits } from 'vue'
import type { UploadResponse } from '@/types/detection'
import { UploadFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

// 定义事件
const emit = defineEmits<{
  (e: 'upload-success', data: UploadResponse): void
}>()

// 上传前的验证函数
const beforeUpload = (file: File) => {
  const isImage = file.type.startsWith('image/')
  const isLt10M = file.size / 1024 / 1024 < 10

  if (!isImage) {
    ElMessage.error('只能上传图片文件！')
    return false
  }
  if (!isLt10M) {
    ElMessage.error('图片大小不能超过 10MB！')
    return false
  }
  return true
}

// 上传成功的回调函数
const handleSuccess = (response: UploadResponse) => {
  ElMessage.success('上传成功')
  emit('upload-success', response)
}

// 上传失败的回调函数
const handleError = () => {
  ElMessage.error('上传失败')
}
</script>

<style scoped>
/* 上传组件样式 */
.upload-demo {
  width: 100%;
}
</style> 