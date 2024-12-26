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
    const url = URL.createObjectURL(file); // 创建临时 URL
    emit("upload-success", { url }); // 触发事件并传递 URL
  }
};
</script>
