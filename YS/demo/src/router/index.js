import Vue from 'vue'
import Router from 'vue-router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import store from '../vuex/store'
// import index from '@/components/index'

// const index = () => import(/* webpackChunkName: "group-foo" */ '../components/index.vue')
Vue.use(ElementUI)
Vue.use(Router)

const router =  new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../pages/login.vue'),
    },
    {
      path: '/',
      redirect: 'login',
    },
  ]
})

router.beforeEach((to, from, next) => {
    // console.log(to.name+"  "+from.name );
    // loginOut
    if (sessionStorage.getItem('loginOut')) {
      sessionStorage.removeItem('loginOut')
      next({path:"/login"})
    }
    // login
    if (sessionStorage.getItem('loginIn')) {
      sessionStorage.removeItem('loginIn')
      router.addRoutes(store.getters.routes)
      next({path:"/index"})
    }
    if (to.name==null&from.name==null) {
      if (sessionStorage.getItem('userName')&&sessionStorage.getItem('userToken')&&sessionStorage.getItem('userRoutes')) {
            store.dispatch("setUser",sessionStorage.getItem('userName'))
            store.dispatch("setToken",sessionStorage.getItem('userToken'))
            store.dispatch('generateNavAndRoutes',JSON.parse(sessionStorage.getItem('userRoutes')))
            store.dispatch("setPermissionDict",JSON.parse(sessionStorage.getItem('permissionDict')))
            router.addRoutes(store.getters.routes)
            router.replace(window.location.href.split("#")[1]) //replace,保证浏览器回退的时候能直接返回到上个页面，不会叠加
      }
    }


    //验证是否登陆
    // if(to.name === 'login') {
    //   if (store.getters.isLogin) {
    //     sessionStorage.setItem('errorToLogin',true)
    //     console.log(sessionStorage.getItem('errorToLogin'));
    //     next({path: '/index'})
    //   }else{
    //     if (sessionStorage.getItem('userName')&&sessionStorage.getItem('userToken')&&sessionStorage.getItem('userRoutes')) {
    //       store.dispatch("setUser",sessionStorage.getItem('userName'))
    //       store.dispatch("setToken",sessionStorage.getItem('userToken'))
    //       store.dispatch('generateNavAndRoutes',JSON.parse(sessionStorage.getItem('userRoutes')))
    //       router.addRoutes(store.getters.routes)
    //       sessionStorage.setItem('errorToLogin',true)
    //       next({path: '/index'})
    //     }else {
    //       sessionStorage.clear()
    //     }
    //   }
    //   next()
    // }

    next()
})

router.afterEach((to, from) => {
  // sessionStorage.setItem('new',to.name)
})

export default router;
