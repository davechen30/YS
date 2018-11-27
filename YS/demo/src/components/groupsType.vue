<template>
  <el-card class="con-container">
    <div class="con" style="height:100%">
      <!-- tag -->
      <div class="search-tag-container">
        <el-tag :key="tag" v-for="tag in dynamicTags" closable :disable-transitions="false" @close="handleClose(tag)">
          {{tag}}
        </el-tag>
        <div  class="input-new-tag"  v-if="inputVisible"  ref="saveTagInput" size="mini" >
          <div style="margin-top: 5px;">
            <el-input placeholder="请输入内容"   ref="saveTagInput"  @keyup.enter.native="handleInputConfirm" v-model="inputValue" class="input-with-select">
              <el-select v-model="select" slot="prepend" placeholder="请选择">
                <div v-for="(item,key) in table_column" :key="item.key">
                  <el-option :label="item" :value="key"></el-option>
                </div>
              </el-select>
              <el-button slot="append" icon="el-icon-plus" @click="handleInputConfirm" ></el-button>
            </el-input>
          </div>
        </div>
      </div>
      <!-- tag -->
      <!-- button-nav -->
      <div class="button-nav-container" style="margin-top: 5px;">
        <el-button @click="initDatas">刷新数据</el-button>
        <el-button v-if="!inputVisible" style='margin-left:0px;' @click="showInput">+筛选条件</el-button>
        <add-from
          :class="butShow.add?'button-nav':'button-nav-hidden'"
          :choices_field_dict="choices_field_dict"
          :data_field_type="data_field_type"
          :table_column="table_column"
          :add_form="add_form"
          :modelname="model"
          @reloadData="initDatas"
      ></add-from>
        <update-from
          :class="butShow.change?'button-nav':'button-nav-hidden'"
          :choices_field_dict="choices_field_dict"
          :data_field_type="data_field_type"
          :table_column="table_column"
          :update_form="update_form"
          :modelname="model"
          :disable="multipleSelection.length==1?false:true"
          @reloadData="initDatas"
          display="none"></update-from>
        <collapse-from
          :permissionslist="permissionslist"
          :childGroup="group"
          :permissionChange="butShow.change"
          :class="butShow.view?'button-nav':'button-nav-hidden'"
          :disable="multipleSelection.length==1?false:true"
          @reloadData="initDatas"
        ></collapse-from>
        <el-button
          :class="butShow.delete?'button-nav':'button-nav-hidden'"
          @click="delMsg"
          :disabled="this.multipleSelection.length>0?false:true"
          >批量删除</el-button>
      </div>
      <!-- button-nav -->
      <!-- container -->
      <div class="container" style="margin-top: 5px;">
        <template>
          <el-table :data="table_show_data" border  style="width: 100%" @selection-change="handleSelectionChange">
            <el-table-column class="el-table-column-selection" type="selection" fixed="left">
            </el-table-column>
            <div v-for="(item,key) in table_column" :key="item.key">
                <el-table-column :prop="key" min-width="150px;" :label="item" ></el-table-column>
            </div>
          </el-table>
        </template>
      </div>
      <!-- container -->
      <!-- 分页 -->
      <div class="pagination">
        <div class="block">
         <el-pagination
           @size-change="handleSizeChange"
           @current-change="handleCurrentChange"
           :current-page="pagination.current_page"
           :page-sizes="[5, 10, 15, 20]"
           :page-size="pagination.page_size"
           layout="total, sizes, prev, pager, next, jumper"
           :total="pagination.data_size">
         </el-pagination>
       </div>
      </div>
      <!-- 分页 -->
    </div>
  </el-card>
</template>

<script>
import {getMsg,delMsg,downloadExcel} from "../api/api"
import addFrom from "./addFrom"
import updateFrom from "./updateFrom"
import collapseFrom from "./collapseFrom"
export default {
  components:{
    addFrom,updateFrom,collapseFrom
  },
  data() {
    return {
      user:'dave',
      model: '',
      lowermodel: '',
      table_data: [],
      table_show_data:[],
      data_field_type: {},
      table_column: {},
      dynamicTags: [],//查询
      search_field: {},
      search_field_datas: [],
      inputVisible: false,
      inputValue: '',
      select: '',
      add_form: {},
      update_form: {},
      multipleSelection: [],  //选择项
      choices_field_dict:{},
      permissionslist:[],
      group:{},
      butShow:{
        add:false,
        change:false,
        delete:false,
      },
      pagination:{//分页
        page_size: 10,
        data_size: 0,
        current_page: 0,
      }
      // order: id,
    }
  },
  methods: {
// 每页数据大小
    handleSizeChange(val) {
      this.pagination.page_size = val
      this.initDatas()
    },
// 当前页
    handleCurrentChange(val) {
      this.pagination.current_page = val
      this.next_page()
    },
// 删除tag
    handleClose(tag) {
      let w = this.dynamicTags.indexOf(tag)
      this.dynamicTags.splice(w, 1);
      this.search_field_datas.splice(w, 1);
      this.search_field = {}
      for (var i = 0; i < this.search_field_datas.length; i++) {
        for(var key in this.search_field_datas[i]){
          if(this.search_field[key]){
            this.search_field[key].push(this.search_field_datas[i][key]);
          }else {
            this.search_field[key] = [this.search_field_datas[i][key]];
          }
        }
      }
      this.initDatas()
    },
// 显示tag输入框
    showInput() {
      this.inputVisible = true;
    },
// 添加tag
    handleInputConfirm() {
      let inputValue = this.inputValue.replace(/^\s+|\s+$/g,"");
      let select = this.select
      if (inputValue&&this.select) {
        let showValue = this.table_column[this.select] + "：" + inputValue;
        if(this.search_field[this.select]){
          this.search_field[this.select].push(inputValue);
        }else {
          this.search_field[this.select] = [inputValue];
        }
        let dic = {};
        dic[this.select] = inputValue;
        this.search_field_datas.push(dic);
        this.dynamicTags.push(showValue);
        this.initDatas()
      }
      this.inputVisible = false;
      this.inputValue = '';
      this.select = ''
    },
// 更新所选择集合
    handleSelectionChange(val) {
      this.multipleSelection = val;
      if (this.multipleSelection.length == 1) {
        this.group = {
          'name':'',
          'showpermissions':[],
          'permissions':[],
        }
        this.group = this.multipleSelection[0]
      }
      for (var key in this.multipleSelection[0]) {
        if (key === 'permissions'|key === 'showpermissions') {
          continue
        }
        this.update_form[key] = this.multipleSelection[0][key]
      }
    },
// 响应数据刷新
    next_page() {
      getMsg({
        'model': this.model,
        'search_field':JSON.stringify(this.search_field),
        'page_size':this.pagination.page_size,
        'current_page':this.pagination.current_page,
      }).then((response)=>{
        this.table_data = response.data.data
        this.table_column = response.data.column
        this.pagination.data_size = response.data.dataSize
        this.table_show_data = response.data.data
        this.choices_field_dict = response.data.choicesFieldDict
        this.permissionslist = response.data.permissionslist
        for (var key in this.data_field_type) {
          if (this.data_field_type[key]==='BooleanField') {
            for (var itemKey in this.table_show_data) {
              if (this.table_show_data[itemKey][key]) {
                this.table_show_data[itemKey][key] = "是"
              }else {
                this.table_show_data[itemKey][key] = "否"
              }
            }
          }
        }
      })
    },
// 查找数据
    initDatas() {
      getMsg({
        'model': this.model,
        'page_size':this.pagination.page_size,
        'search_field':JSON.stringify(this.search_field),
        'current_page':1})
      .then((response)=>{
        this.data_field_type = response.data.fieldType
        this.table_data = response.data.data
        this.table_show_data = response.data.data
        this.permissionslist = response.data.permissionslist
        for (var key in this.data_field_type) {
          if (this.data_field_type[key]==='BooleanField') {
            for (var itemKey in this.table_show_data) {
              if (this.table_show_data[itemKey][key]) {
                this.table_show_data[itemKey][key] = "是"
              }else {
                this.table_show_data[itemKey][key] = "否"
              }
            }
          }
        }
        this.table_column = response.data.column
        this.pagination.data_size = response.data.dataSize
        this.choices_field_dict = response.data.choicesFieldDict
        this.add_form = {}
        for (var i in this.data_field_type) {
          switch (this.data_field_type[i]) {
            case 'BooleanField':
              this.add_form[i] = false
              break;
            case 'CharField':
              this.add_form[i] = ''
              break;
            case 'ChoicesField':
              this.add_form[i] = ""
              break;
            default:
          }
        }
        if (this.table_data.length>0) {
          this.pagination.current_page = 1
        }
      })
    },
// 删除请求
    delMsg(){
      let _this = this
      let keys = []
      for (var item in _this.multipleSelection) {
        for (var key in _this.multipleSelection[item]) {
          if (key == 'id') {
              keys.push(_this.multipleSelection[item][key])
          }
        }
      }
      if (keys.length!=0) {
        delMsg({
        'model':this.model,
        'keys':JSON.stringify(keys),
        })
        .then((response) => {
          this.initDatas()
        })
      }
    },
  },

  watch:{
    '$route'(to,from){
      this.butShow = {
        add:false,
        change:false,
        delete:false,
      },
      sessionStorage.setItem("oldPath",to.path)
      this.model = to.params.groupsname
      this.lowermodel = this.model.toLowerCase()
      var permissionDict = this.$store.getters.permissionDict[this.lowermodel]
      console.log("2");
      console.log(this.lowermodel);
      console.log(permissionDict);
      for (var value in permissionDict) {
        this.butShow[value] = permissionDict[value]
      }
      this.initDatas()
    },

  },
  mounted() {
    var starttime = new Date().getTime();
    this.butShow = {
      add:false,
      change:false,
      delete:false,
    },
    this.model = this.$route.params.groupsname
    this.lowermodel = this.model.toLowerCase()
    console.log("1");
    console.log(this.lowermodel);
    var permissionDict = this.$store.getters.permissionDict[this.lowermodel]
    console.log(this.$store.getters.permissionDict);
    for (var value in permissionDict) {
      this.butShow[value] = permissionDict[value]
    }
    this.initDatas()
    var endtime = new Date().getTime();
    console.log(endtime-starttime+"毫秒");
  }
}
</script>

<style  lang="scss">
  .con-container{
    .con {
      position: relative;
      width: 100%;
      .search-tag-container {
        .el-tag{
          margin-right: 5px;
          font-size: 12px;
          margin: 5px;
        }

        .input-new-tag {
          width:450px;
          // margin-left: 10px;
          vertical-align: bottom;
          .input-with-select .el-input-group__prepend {
            width:70px;
            background-color: #fff;
          }
        }
      }

      .button-nav-container{
        text-align:left;
        .button-nav{
          // padding: 7px 10px;
          margin: 0;
        }
        .button-nav-hidden{
          display: none;
          margin: 0;
        }
      }


      .container{
        .el-table-column-selection{
          align: center;
        }
        .el-table-column-header{
          // align: center;
          text-align: center;
        }
        .el-table-column-operation{
          // align: center;
          text-align: center;
        }
      }

      .pagination{

        margin-bottom: 0px;
      }


      .column_show{
        // display: block;
        // visibility: visible;
        min-width: 180px;
      }
      .column_hidden{
        // display: none;
        // visibility: hidden;
        width: 0px;
      }
  }
  }
</style>
