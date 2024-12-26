<template>
  <div>
    <el-upload
      class="upload-demo"
      action=""
      :http-request="handleFileUpload"
      :show-file-list="false"
      accept="image/*"
    >
      <el-button type="primary" :loading="loading">选择图片</el-button>
    </el-upload>
  </div>
</template>

<script setup lang="ts">
import { defineEmits } from "vue";
import { defineProps } from "vue";

defineProps({
  loading: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["upload-success"]);

const handleFileUpload = (options: { file: File }) => {
  const file = options.file;

  if (file) {
    const maxSize = 5 * 1024 * 1024; // 5MB
    const validTypes = ["image/jpeg", "image/png", "image/gif", "image/bmp", "image/webp"]; // 允许的文件类型

    if (file.size > maxSize) {
      alert("文件大小不能超过5MB");
      return;
    }

    if (!validTypes.includes(file.type)) {
      alert("文件类型必须为图片格式");
      return;
    }

    const url = URL.createObjectURL(file); // 创建临时 URL
    emit("upload-success", { url }); // 触发事件并传递 URL
  }
};
</script>
