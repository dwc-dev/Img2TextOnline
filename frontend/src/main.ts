// 导入 Vue 核心功能和类型定义
import { createApp, Component } from 'vue'
// 导入 Element Plus UI 框架
import ElementPlus from 'element-plus'
// 导入 Element Plus 的样式文件
import 'element-plus/dist/index.css'
// 导入 Element Plus 的所有图标组件
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// 导入根组件
import App from './App.vue'
// 导入路由配置
import router from './router/index'

// 创建 Vue 应用实例
const app = createApp(App)

// 全局注册所有 Element Plus 图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component as Component)
}

// 使用 Element Plus 插件
app.use(ElementPlus)
// 使用路由插件
app.use(router)
// 将应用挂载到 DOM 上
app.mount('#app')
