import router from '../router/index'
// import componentlist from '../util/componentList'


export const setUser = ({commit},user) => {
  commit("setUser",user)
}

export const setToken = ({commit},token) => {
  commit("setToken",token)
}

export const setPermissionDict = ({commit},permissionDict) => {
  commit("setPermissionDict",permissionDict)
}

export const generateNavAndRoutes = ({commit},data) => {

  if (data) {
    let routesData = data.routes
    let componentList = data.componentList
    for (var key in componentList) {
      let component_code = componentList[key].code
      let path = componentList[key].path
      let temp = {
        path: path,
        name: component_code,
        component: resolve => require(["../components/" + component_code + ".vue"], resolve),
      }
      // console.log(temp);
      commit('addRoutes',temp);
    }
    let routes = []
    for (var i=0; i < routesData.length; i++){
      if (routesData[i].is_root) {
        // 生成菜单
        let code = routesData[i].code
        let children = []
        let name = routesData[i].name
        let icon = routesData[i].icon
        for (var j=0; j < routesData.length; j++){
          if (routesData[j].father_code == code) {
            children.push({
              path: routesData[j].href,
              icon: routesData[j].icon,
              name: routesData[j].name,
            })
          }
        }
        let navItem = {
          name: name,
          icon: icon,
          children: children,
        }
        commit('addNavItem',navItem)
      }
    }
    commit('addOtherRoutes');
  }
}


export const loginOut = ({commit}) => {
  sessionStorage.clear()
  sessionStorage.setItem('loginOut',true)
  commit('loginOut')
}
