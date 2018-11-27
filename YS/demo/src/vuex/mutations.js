export const setUser = (state,user) => {
  if (user) {
    state.userName = user
    state.isLogin = true
  }else if (user==null) {
    // sessionStorage.setItem("userName",null);
    // sessionStorage.setItem("userToken","");
    state.userName = null;
    state.isLogin = false;
    state.token = "";
  }
}
export const setSysName = (state,sysName) => {
  if (sysName) {
    state.sysName = sysName
  }
}
export const setPermissionDict = (state,permissionDict) => {
  if (permissionDict) {
    state.permissionDict = permissionDict
  }
}
export const setToken = (state,token) => {
  if(token){
    state.token = token
  }
}

export const addNavItem = (state,navItem) => {
    state.navList.push(navItem)
}

export const addRoutes = (state,routes) => {
    state.routes[0].children.push(routes)
}

export const addOtherRoutes = (state) => {
    state.routes.push(
      {
        path: '/',
        redirect: { name: 'login' },
      }
    )
}

export const loginOut = (state) => {
  state.userName = null
  state.navList = []
  state.routes = [
    {
      path: '/index',
      // redirect: '/first',
      name: 'index',
      component: () => import('../pages/index.vue'),
      children:[]
    }
  ]
  state.token = null
  state.isLogin = false
}
