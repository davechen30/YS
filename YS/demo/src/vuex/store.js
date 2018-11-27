import Vue from 'vue'
import Vuex from 'vuex'
import * as getters from './getters'
import * as actions from './actions'
import * as mutations from './mutations'
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    sysName: '原昇',
    userName : null,
    isLogin: false,
    token: null,
    navList: [],
    permissionDict:{},
    // componentType:
    routes : [
      {
        path: '/index',
        // redirect: '/first',
        name: 'index',
        component: () => import('../pages/index.vue'),
        children:[]
      }
    ],
  },
  getters,
  actions,
  mutations,
})

export default store
