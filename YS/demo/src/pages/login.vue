<template>
  <el-form :model="loginForm" status-icon :rules="loginRules" ref="loginForm" label-position="left" label-width="0px" class="loginForm">
    <h3 class="title">系统登录</h3>
    <el-form-item prop="username">
      <el-input v-model="loginForm.username" autocompplete="off" placeholder="账号"></el-input>
    </el-form-item>
    <el-form-item prop="password">
      <el-input type="password" v-model="loginForm.password" autocompplete="off" placeholder="密码"></el-input>
    </el-form-item>
    <el-button type="primary" style="width:100%;" @click.native.prevent="onSubmit">登陆</el-button>
  </el-form>
</template>
<script>
  import {login} from "../api/api"
  // import {getCookie} from "../util/util"
  import router from '../router/index'
  export default {
    data() {
      return {
        loginForm : {
          username: 'root',
          password: '123',
        },
        loginRules:{
          username: [
            { required: true, message: '请输入账号', trigger: 'blur' },
            //{ validator: validaePass }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            //{ validator: validaePass }
          ],
        }
      }
    },
    methods:{
      onSubmit: function(event) {
        var starttime = new Date().getTime();
        if (this.$store.getters.isLogin == true) {
          this.$router.push({path: '/index'})
        }else {
        login({'username':this.loginForm.username,'password':this.loginForm.password})
          .then((response) => {
            if (response.data.code == 1) {
              // this.$store.state.token = response.data.token
              // console.log(JSON.parse(response.data.routes));
              sessionStorage.setItem("userName",response.data.username)
              sessionStorage.setItem("userToken",response.data.token)
              sessionStorage.setItem("userRoutes",response.data.routes)
              sessionStorage.setItem("permissionDict",response.data.permissionDict)
              this.$store.dispatch("setUser",response.data.username)
              this.$store.dispatch("setToken",response.data.token)
              this.$store.dispatch('generateNavAndRoutes',JSON.parse(response.data.routes))
              this.$store.dispatch("setPermissionDict",JSON.parse(response.data.permissionDict))
              // this.$router.addRoutes(this.$store.getters.routes)
              sessionStorage.setItem("loginIn",true)
              this.$router.push({path: '/index'})
            }else if (response.data.code == 0) {
              console.log(response.data)
            }
          }).catch(function (res) {
            alert(res.toString())
          })
        }
        var endtime = new Date().getTime();
        console.log(endtime-starttime+"毫秒");
      },
    },
    mounted() {
  }
}
</script>
<style>

  .loginForm{
    /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;

  }
  .title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }

</style>
