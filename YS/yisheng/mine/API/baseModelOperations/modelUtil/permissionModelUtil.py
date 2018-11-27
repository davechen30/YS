from django.db.models import Q

from mine.API.baseModelOperations.modelUtil.ModelUtilAbstract import ModelUtilAbstract
from util.excelUtil import writeExcel
import logging
from django.forms.models import model_to_dict
logger = logging.getLogger(__name__)

class PermissionModelUtil(ModelUtilAbstract):

    # 不输出的字段
    modelFieldExclude = []
    # 不显示的字段
    modelShowFieldExclude = []
    # 不显示的字段类型
    modelFieldTypeExclude = ['id']

    # def getChoicesFieldDict(self):
    #     choicesFieldDict = {}
    #     if hasattr(self.modelobj, 'ChoicesField'):
    #         ModelChoicesFieldDict = self.modelobj.ChoicesField
    #         for field in ModelChoicesFieldDict:
    #             choicesFieldList = []
    #             modeldemo = BaseModelUtil(ModelChoicesFieldDict[field]['model'])
    #             l = modeldemo.getModel().objects.filter().values(*[ModelChoicesFieldDict[field]['field'], 'name'])
    #             for i in l:
    #                 choicesFieldList.append({
    #                     'value': i[ModelChoicesFieldDict[field]['field']],
    #                     'name': i['name']
    #                 })
    #             choicesFieldDict[field] = choicesFieldList
    #     return choicesFieldDict
    def getPostData(self,search_field, current_page, page_size):
        column = self.getModelField()
        data, dataSize = self.getDatas(search_field, current_page, page_size)
        choicesFieldDict = self.getChoicesFieldDict()
        fieldType = self.getModelFieldType()
        datas = {}
        datas['data'] = data
        datas['column'] = column
        datas['dataSize'] = dataSize
        datas['fieldType'] = fieldType
        datas['choicesFieldDict'] = choicesFieldDict
        return datas

    def getDatas(self,search_field,current_page,page_size):
        qand = Q()
        if (search_field.__len__() != 0):
            for search_key in search_field:
                qor = Q()
                qor.connector = Q.OR
                for svalue in search_field[search_key]:
                    # qor.add(Q(**{skey: svalue.strip()}), Q.OR)
                    qor.children.append((search_key, svalue.strip()))
                qand.add(qor, Q.AND)
        if (self.modelName == 'User') & (self.appName=='user'):
            qand.add(~Q(is_active=0), Q.AND)
        else:
            if self.appName != 'auth':
                qand.add(~Q(status=0), Q.AND)
        start = (current_page - 1) * page_size
        end = current_page * page_size
        showList = self.getModelShowField()

        dataList = self.modelobj.objects.filter(qand).values(*showList).order_by('id')[start:end]
        data = []
        for item in dataList:
            data.append(item)
        dataSize = self.modelobj.objects.filter(qand).__len__()
        return data,dataSize

    def getModelField(self):
        """
        获取model的verbose_name和name的字段
        :param appname: app name
        :param modelName: model name
        :param exclude: don`t want field
        """
        fileddic = {}
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelFieldExclude]:
            fileddic[i.name] = i.verbose_name
        return fileddic

    def getModelFieldType(self):
        """
        获取model字段的类型,添加或修改数据用
        :param appname: app name
        :param modelName: model name
        :param exclude: don`t want field
        """
        filedType = {}
        choicesFieldList = []
        if hasattr(self.modelobj, 'ChoicesField'):
            ModelChoicesFieldDict = self.modelobj.ChoicesField
            for field in ModelChoicesFieldDict:
                choicesFieldList.append(field)
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelFieldTypeExclude]:
            if i.name in choicesFieldList:
                filedType[i.name] = 'ChoicesField'
            else:
               filedType[i.name] = type(i).__name__
        return filedType

    def getModelShowField(self):
        """
        获取model展示的字段
        :param appname: app name
        :param modelName: model name
        """
        filedList = []
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelShowFieldExclude]:
            filedList.append(i.name)
        return filedList

    def downloadModelExcel(self):
        # excelName, sheetName, excelColumnName, data
        columnList = []
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name]:
            columnList.append(i.verbose_name)

        alldatas = self.modelobj.objects.all()
        datas = []
        for col in alldatas:
            dataj = []
            dic = model_to_dict(col)
            for row in dic:
                dataj.append(dic[row].__str__())
            datas.append(dataj)
        return writeExcel(self.modelName,columnList,datas)

    def addObj(self,data):
        try:
            self.modelobj.objects.create(**data)
        except Exception as e:
            logger.info(e)
            return False
        return True

    def delObj(self,IdList):
        for id in IdList:
            obj = self.modelobj.objects.filter(Q(id=id))[0]
            obj.status = 0
            obj.save()

    def updateObj(self,updateData):
        obj = self.modelobj.objects.filter(Q(id=updateData['id']))[0]
        for item in updateData:
            setattr(obj, item, updateData[item])
        obj.save()