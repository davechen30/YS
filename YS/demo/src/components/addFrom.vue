<template>
  <span class="add-form">
    <el-button type="button" @click="dialogFormVisible = true">添加</el-button>
    <el-dialog title="添加数据" :visible.sync="dialogFormVisible">
      <el-form status-icon label-width="100px">
        <div v-for="(item,key) in data_field_type" :key="item.key">
          <div v-if="item==='CharField'">
            <el-form-item :label="table_column[key]">
              <el-input v-model="add_form[key]" autocomplete="off"></el-input>
            </el-form-item>
          </div>
          <div v-else-if="item==='BooleanField'">
            <el-form-item :label="table_column[key]">
              <input type="checkbox" @change="addCheckBoxChange(key)" :checked="add_form[key]"/>
            </el-form-item>
          </div>
          <div v-else-if="item==='ChoicesField'">
            <el-form-item :label="table_column[key]">
              <select :id="key" v-model="add_form[key]">
                <option disabled value="">请选择</option>
                <option v-for="subitem in choices_field_dict[key]" :value="subitem.value">{{subitem.name}}</option>
              </select>
            </el-form-item>
          </div>
        </div>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addMsg(modelname,add_form)">确 定</el-button>
      </div>
    </el-dialog>
  </span>
</template>
<script>
import {addMsg} from "../api/api"
  export default {
    name:'addFrom',
    props: {
      data_field_type:{
        type: Object
      },
      table_column:{
        type: Object
      },
      add_form:{
        type: Object
      },
      modelname: {
        type: String
      },
      choices_field_dict:{
        type: Object
      }
    },
    data() {
      return {
        dialogFormVisible: false,
        select:'',
        item:'',
        dict:{},
        id:'',
      };
    },
    methods: {
    // 添加请求
      addMsg(modelname,add_form){
        addMsg({
        'model':modelname,
        'data':add_form,})
        .then((response) => {
          if (response.data.code==1) {
            this.dialogFormVisible = false
            this.$emit('reloadData')
          }
        })
      },
      addCheckBoxChange(key){
        this.add_form[key] = !this.add_form[key]
      },
    }
  };
</script>
<style>
select{
  /* appearance:none;
  -moz-appearance:none;
  -webkit-appearance:none;
  -ms-appearance:none; */
  border:1px solid #CCC;
  width:230px;
  height:44px;
  border-radius: 5px;
  /* background:url("../../static/image/menu.png") no-repeat scroll right center #fff;
  background:#fff\9; */
  color:#666;
  padding:8px;
  outline:none;
}
.dialog-footer{
  text-align: center;
}
</style>
