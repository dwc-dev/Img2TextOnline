// 为 .vue 文件声明类型定义
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

// 为 Element Plus 声明模块定义
declare module 'element-plus'
// 为 Element Plus 图标声明模块定义
declare module '@element-plus/icons-vue'
// 为 Vue Router 声明模块定义
declare module 'vue-router' 