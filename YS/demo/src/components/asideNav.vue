<template>
  <aside :class="collapsed?'menu-collapsed':'menu-expanded'">
    <el-menu default-active="1" class="el-menu-vertical-demo" :collapse="collapsed">
      <div v-for="(item,index) in sysNav">
        <el-submenu :index="index+1+''">
          <!-- {{index+1+''}} -->
          <template slot="title">
            <i :class="item.icon"></i>
            <span slot="title" :class="collapsed?'nav-item-hidden':'nav-item-show'">{{item.name}}</span>
          </template>
          <div v-for="(subItem,subindex) in item.children">
            <!-- {{(index+1)+'-'+(subindex+1)}} -->
            <router-link :to="subItem.path"><el-menu-item :index="(index+1)+'-'+(subindex+1)"><i :class="subItem.icon"></i>{{subItem.name}}</el-menu-item></router-link>
          </div>
        </el-submenu>
      </div>
    </el-menu>
  </aside>
</template>
<script>
export default {
    name: 'asideNav',
    props: {
      collapsed:{
        type: Boolean
      },
      sysNav: {
        type: Array
      }
    },
    methods: {
          handleClick (e) {
            e.preventDefault()
            e.target.parentElement.classList.toggle('open')
          },
          addActive(e){
             e.preventDefault()
            e.target.parentElement.parentElement.parentElement.classList.add('open')
          }
      },
      mounted(){
              console.log(this.routes)
      }
  }
</script>

<style scoped lang="scss">

    aside {
      flex:0 0 230px;
      width: 230px;
      a{
        text-decoration: none;
      }
      .el-menu-item {
        text-decoration: none;
      }
      .el-submenu__title{
        text-decoration: none;
      }

      .el-menu{
        height: 100%;
      }
      .collapsed{
        width:60px;
        .item{
          position: relative;
        }
        .submenu{
          position:absolute;
          top:0px;
          left:60px;
          z-index:99999;
          height:auto;
          display:none;
        }

      }
    }
    .nav-item-show{
    }
    .nav-item-hidden{
      display: none;
    }
    .menu-collapsed{
      flex:0 0 60px;
      width: 60px;
    }
    .menu-expanded{
      flex:0 0 230px;
      width: 230px;
    }


</style>
