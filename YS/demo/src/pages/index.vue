<template>
  <el-row class="container">
    <el-col :span="24" class="header">
      <el-col :span="10" class="logo" :class="collapsed?'logo-collapse-width':'logo-width'">
        {{collapsed?'':sysName}}
      </el-col>
      <el-col :span="10">
        <div class="tools" @click.prevent="collapse">
          <i class="el-icon-menu"></i>
        </div>
      </el-col>
      <el-col :span="4" class="userinfo">
        <el-dropdown trigger="hover">
          <span class="el-dropdown-link userinfo-inner">
            <!-- <img :src="this.sysUserAvatar" />  -->
            {{sysUserName}}</span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>我的消息</el-dropdown-item>
            <el-dropdown-item>设置</el-dropdown-item>
            <el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-col>
    <el-col :span="24" class="main">
      <!-- 导航 -->
      <aside-nav :collapsed='collapsed' :sysNav="sysNav"></aside-nav>
      <!-- 容器 -->
      <section class="content-container">
        <router-view >jojaoj</router-view>
      </section>
    </el-col>
  </el-row>
</template>

<script>
import asideNav from '@/components/asideNav';
export default {
  components:{ asideNav },
  data() {
    return {
      sysName:'',
      collapsed:false,
      sysUserName: '',
      sysUserAvatar: '',
      sysNav: [],
    }
  },
  methods: {
    onSubmit() {
      console.log('submit!');
    },
    //退出登录
    logout: function () {
      var _this = this;
      this.$confirm('确认退出吗?', '提示', {
        //type: 'warning'
      }).then(() => {
        this.$store.dispatch('loginOut')
        window.location.reload()
      }).catch(() => {
      });
    },
    //折叠导航栏
    collapse:function(){
      this.collapsed=!this.collapsed;
    },
    showMenu(i,status){
      this.$refs.menuCollapsed.getElementsByClassName('submenu-hook-'+i)[0].style.display=status?'block':'none';
    }
  },
  mounted() {
    this.sysName = this.$store.getters.sysName
    this.sysUserName = this.$store.getters.userName
    this.sysNav = this.$store.getters.navList
  }
}
</script>

<style scoped lang="scss">

.container {
  position: absolute;
  top: 0px;
  bottom: 0px;
  left: 0px;
  width: 100%;
  img {
    width: 35px;
    height: 35px;
    border-radius: 20px;
    margin: 10px -10px 10px 10px;
    float: right;
  }
  .header {
    height: 60px;
    line-height: 60px;
    background: #20a0ff;
    color:#fff;
    .userinfo {
      text-align: right;
      padding-right: 35px;
      float: right;
      .userinfo-inner {
        cursor: pointer;
        color:#fff;
        img {
          width: 40px;
          height: 40px;
          border-radius: 20px;
          margin: 10px 0px 10px 10px;
          float: right;
        }
      }
    }
    .logo {
      //width:230px;
      height:60px;
      font-size: 22px;
      padding-left:20px;
      padding-right:20px;
      border-color: rgba(238,241,146,0.3);
      border-right-width: 1px;
      border-right-style: solid;
      img {
        width: 40px;
        float: left;
        margin: 10px 10px 10px 18px;
      }
      .txt {
        color:#fff;
      }
    }
    .logo-width{
      width:230px;
    }
    .logo-collapse-width{
      width:65px
    }
    .tools{
      padding: 0px 23px;
      width:14px;
      height: 60px;
      line-height: 60px;
      cursor: pointer;
    }
  }
  .main {
    display: flex;
    // background: #324057;
    position: absolute;
    top: 60px;
    bottom: 0px;
    overflow: hidden;
    text-align: left;
    aside {
      flex:0 0 230px;
      width: 230px;
      // position: absolute;
      // top: 0px;
      // bottom: 0px;
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
    .content-container {
      // background: #f1f2f7;
      flex:1;
      // position: relative;
      // right: -5px;
      // top: 0px;
      // bottom: 0px;
      // left: 230px;
      padding: 5px;
      overflow-y: scroll;
      .breadcrumb-container {
        //margin-bottom: 15px;
        .title {
          width: 200px;
          float: left;
          color: #475669;
        }
        .breadcrumb-inner {
          float: right;
        }
      }
      .content-wrapper {
        background-color: #fff;
        box-sizing: border-box;
      }
    }
  }
}

</style>
