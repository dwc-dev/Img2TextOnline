<template>
  <div>
    <!-- 上传逻辑 -->
    <input type="file" @change="handleFileUpload" />
  </div>
</template>

<script setup lang="ts">
import { defineEmits } from 'vue'

const emit = defineEmits(['upload-success'])

const handleFileUpload = (event: Event) => {
  const input = event.target as HTMLInputElement;
  const file = input.files?.[0]; // 使用可选链操作符

  if (file) {
    const url = URL.createObjectURL(file); // 创建临时 URL
    emit('upload-success', { url }); // 触发事件并传递 URL
  }
}
</script> 