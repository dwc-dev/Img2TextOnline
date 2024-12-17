// 检测结果对象类型定义
export interface DetectionObject {
  // 检测到的目标类别
  class: string
  // 检测的置信度（0-1之间的数值）
  confidence: number
  // 边界框坐标 [x, y, width, height]
  bbox: [number, number, number, number]
}

// 检测结果类型定义
export interface DetectionResult {
  // 检测到的所有目标对象数组
  objects: DetectionObject[]
}

// 上传响应类型定义
export interface UploadResponse {
  // 上传后的图片URL
  url: string
  // 检测结果
  result: DetectionResult
} 