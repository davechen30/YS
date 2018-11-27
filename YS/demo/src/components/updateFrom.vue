<template>
  <span class="update-from">
    <el-button type="button" @click="dialogFormVisible = true" :disabled="disable">编辑</el-button>
    <el-dialog title="编辑数据" :visible.sync="dialogFormVisible">
      <el-form status-icon label-width="100px">
        <div v-for="(item,key) in data_field_type" :key="item.key">
          <div v-if="item==='CharField'">
            <el-form-item :label="table_column[key]">
              <el-input v-model="update_form[key]" autocomplete="off"></el-input>
            </el-form-item>
          </div>
          <div v-else-if="item==='BooleanField'">
            <el-form-item :label="table_column[key]">
              <input type="checkbox" @change="updateCheckBoxChange(key)" :checked="update_form[key]"/>
              <!-- <el-checkbox @change="updateCheckBoxChange(key)" :checked="update_form[key]"></el-checkbox> -->
            </el-form-item>
          </div>
          <div v-else-if="item==='ChoicesField'">
            <el-form-item :label="table_column[key]">
              <select :id="key" v-model="update_form[key]">
                <option disabled value="">请选择</option>
                <option v-for="subitem in choices_field_dict[key]" :value="subitem.value" >{{subitem.name}}</option>
              </select>
            </el-form-item>
          </div>
        </div>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateMsg(modelname,update_form)">确 定</el-button>
      </div>
    </el-dialog>
  </span>
</template>
<script>
import {updateMsg} from "../api/api"
  export default {
    name:'updateFrom',
    props: {
      data_field_type:{
        type: Object
      },
      table_column:{
        type: Object
      },
      update_form:{
        type: Object
      },
      modelname: {
        type: String
      },
      choices_field_dict:{
        type: Object
      },
      disable: {
        type: Boolean
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
      updateMsg(modelname,update_form){
        updateMsg({
          'model':modelname,
          'datas':{'data':update_form},
        }).then((response) => {
          if (response.data.code==1) {
            this.dialogFormVisible = false
            this.$emit('reloadData')
          }
        })
      },
      updateCheckBoxChange(key){
        this.update_form[key]=!this.update_form[key]
      },
    }
  };
</script>
<style>
.dialog-footer{
  text-align: center;
}
</style>
