// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/theme-chalk/display.css'
import axios from '@/http'
import Header from '@/components/common/Header'
import Footer from '@/components/common/Footer'
import VueResource from 'vue-resource'


// 加载相关组件
Vue.use(ElementUI)
Vue.use(VueResource)

Vue.config.productionTip = false

// 引用常用模板
Vue.component("Header", Header)
Vue.component("Footer", Footer)

// 设置快捷用法
Vue.prototype.axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
