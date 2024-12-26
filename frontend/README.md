# Img2TextOnline (Frontend)

这是 Img2TextOnline 项目的前端部分，使用 Vue 3 和 Element Plus 实现。该项目允许用户上传图片，并通过后端 API 提取图片中的文字。

## 功能特点

- 图片上传与预览
  - 支持拖拽上传
  - 支持点击上传
  - 文件类型限制（jpg/png）
  - 文件大小限制（10MB）
- 检测结果展示
  - 实时显示检测框
  - 显示目标类别和置信度
  - 表格形式展示详细信息
- 用户友好的界面
  - 响应式设计
  - 操作提示
  - 错误反馈

## 技术栈

### 前端

- Vue 3 - 渐进式 JavaScript 框架
- TypeScript - JavaScript 的超集，添加了类型系统
- Element Plus - Vue 3 的组件库
- Vue Router - 官方路由管理器
- Axios - HTTP 客户端

## 前端结构

```
frontend/
├── public/                 # 静态资源
├── src/
│   ├── components/        # 通用组件
│   │   ├── ImageUpload.vue    # 图片上传组件
│   │   └── DetectionResult.vue # 检测结果展示组件
│   ├── router/            # 路由配置
│   ├── types/             # TypeScript 类型定义
│   ├── views/             # 页面组件
│   ├── App.vue           # 根组件
│   └── main.ts           # 入口文件
├── package.json          # 项目配置
└── tsconfig.json         # TypeScript 配置
```

## 项目启动

### 环境要求

- Node.js >= 14.0.0
- Yarn >= 1.22.0

### 安装依赖

```bash
yarn install
```

### 开发环境启动

```bash
yarn serve
```

### 生产环境构建

```bash
yarn build
```

### 代码格式检查

```bash
yarn lint
```

### Docker启动

```bash
docker-compose up
```
tips:注意配置好正确的后端接口地址

## 注意事项

- 确保后端服务已启动并监听 8080 端口
- 上传图片大小不超过 10MB
- 仅支持 jpg/png 格式的图片
- 首次运行请先安装依赖
