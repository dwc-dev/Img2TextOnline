<template>
  <!-- 检测结果容器 -->
  <div class="detection-result">
    <!-- 图片和检测框的容器 -->
    <div class="image-container">
      <!-- 显示上传的图片 -->
      <el-image :src="imageUrl" fit="contain" />
      <!-- 用于绘制检测框的画布，覆盖在图片上方 -->
      <canvas ref="canvas" class="detection-canvas"></canvas>
    </div>
    <!-- 检测结果信息表格区域 -->
    <div class="result-info">
      <el-table :data="resultData" stripe>
        <!-- 目标类别列 -->
        <el-table-column prop="class" label="类别" />
        <!-- 置信度列，显示百分比 -->
        <el-table-column prop="confidence" label="置信度">
          <template #default="scope">
            {{ (scope.row.confidence * 100).toFixed(2) }}%
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup lang="ts">
// 导入必要的 Vue 组件和类型
import { ref, onMounted, watch, defineProps } from 'vue'
import type { DetectionResult, DetectionObject } from '@/types/detection'

// 定义组件属性
const props = defineProps<{
  imageUrl: string    // 图片URL
  result: DetectionResult  // 检测结果数据
}>()

// 画布引用，用于绘制检测框
const canvas = ref<HTMLCanvasElement | null>(null)
// 检测结果数据，用于表格显示
const resultData = ref<DetectionObject[]>([])

// 绘制检测框和标签的函数
const drawDetections = () => {
  // 检查画布和结果是否存在
  if (!canvas.value || !props.result) return
  const ctx = canvas.value.getContext('2d')
  if (!ctx) return

  // 遍历每个检测对象，绘制边界框和标签
  props.result.objects.forEach((obj: DetectionObject) => {
    // 解构边界框坐标
    const [x, y, w, h] = obj.bbox
    // 设置边界框样式
    ctx.strokeStyle = '#409EFF'  // 使用 Element Plus 主题蓝
    ctx.lineWidth = 2
    // 绘制边界框
    ctx.strokeRect(x, y, w, h)
    
    // 绘制标签文本
    ctx.fillStyle = '#409EFF'
    ctx.fillText(`${obj.class} ${(obj.confidence * 100).toFixed(2)}%`, x, y - 5)
  })
}

// 监听检测结果变化，重新绘制检测框
watch(() => props.result, drawDetections, { deep: true })

// 组件挂载后初始化绘制
onMounted(() => {
  drawDetections()
})
</script>

<style scoped>
/* 检测结果容器样式 */
.detection-result {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* 图片容器样式，用于定位画布 */
.image-container {
  position: relative;
  width: 100%;
}

/* 检测框画布样式，覆盖在图片上方 */
.detection-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;  /* 允许点击穿透到下方图片 */
}

/* 结果信息表格样式 */
.result-info {
  margin-top: 20px;
}

/* 图片样式 */
.el-image {
  width: 100%;
  max-height: 500px;
}
</style> 