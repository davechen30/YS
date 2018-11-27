<template>
  <span>
    <el-button type="button" @click="dialogFormVisible = true" :disabled="disable">查看权限</el-button>
    <el-dialog :title="'权限|'+childGroup.name" :visible.sync="dialogFormVisible" width="30%">
      <span :class="change?'change':'view'">
        <!-- kan  -->
        <el-tree
          class="viewtree"
          empty-text="无权限数据"
          :data="childGroup.showpermissions"
          node-key="id">
        </el-tree>
        <el-button :class="permissionChange?'can':'cant'" @click="change = true">修改</el-button>
      </span>
      <span id="changeBox" :class="change?'view':'change'">
        <el-tree
          class="changetree"
          empty-text="无权限数据"
          :data="permissionslist"
          :default-checked-keys="childGroup.permissions"
          show-checkbox
          node-key="id"
          ref="tree">
        </el-tree>
        <div class="butarea">
          <el-button  @click="change = false">返回</el-button>
          <el-button  @click="dialogFormVisible = false">取消</el-button>
          <el-button type="primary"  @click="updateMsg">确定</el-button>
        </div>
      </span>
    </el-dialog>
  </span>
</template>
<script>
import {updateMsg} from "../api/api"
export default{
  name: 'collapseFrom',
  data() {
    return {
      dialogFormVisible: false,
      change:false,
      defaultPermission:[],
    };
  },
  props: {
    disable: {
      type: Boolean
    },
    permissionChange: {
      type: Boolean
    },
    permissionslist:{
      type: Array
    },
    childGroup: {
      type: Object
    },
  },
  methods: {
    updateMsg() {
      updateMsg({
        'model':'auth_Group',
        'datas':{
          'data':this.childGroup,
          'newPermissions':this.$refs.tree.getCheckedKeys(true)},
      }).then((response) => {
        if (response.data.code==1) {
          this.dialogFormVisible = false
          this.$emit('reloadData')
        }
      })
    },
  },
  watch:{
    dialogFormVisible:{
      handler(newValue, oldValue) {
        this.change = false
        if (newValue) {

          // console.log(this.$refs.tree.getCheckedKeys(true));
          // this.$refs.tree2.setCheckedKeys(this.childGroup['permissions'])
        }
      }
    },
    change:{
      handler(newValue, oldValue) {
        this.$refs.tree.setCheckedKeys(this.childGroup['permissions'])
      }
    }
  },
  mounted() {
    this.change = false
  }
}
</script>
<style>
  .can{
    margin: 0 auto;
    display: block;
  }
  .cant{
    display: none;
  }
  .butarea{
    margin: 0 auto;
    margin-top: 10px;
    text-align: center;
  }
  .view{
    display: block;
  }
  .change{
    display: none;
  }
</style>
