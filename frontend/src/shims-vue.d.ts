/* eslint-disable */
// 声明 .vue 文件的模块类型
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  // 定义组件类型
  const component: DefineComponent<{}, {}, any>
  export default component
}
