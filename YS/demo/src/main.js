// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import axios from 'axios'
import store from './vuex/store'
// import funcModule from './components/index.js'
Vue.prototype.$axios = axios
axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.headers.get['Content-Type'] = "application/json"
Vue.config.productionTip = false

// axios.defaults.withCredentials = true
// axios.interceptors.request.use((config) => {
//   config.headers['X-Requested-With'] = 'XMLHttpRequest';
//   let regex = /.*csrftoken=([^;.]*).*$/;
//   config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
//   return config
// });
// Vue.use(funcModule);



/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
