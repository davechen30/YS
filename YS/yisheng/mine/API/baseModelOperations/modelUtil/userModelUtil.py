from django.contrib.auth.models import Group
from django.db.models import Q
from mine.API.baseModelOperations.modelUtil.ModelUtilAbstract import ModelUtilAbstract
from mine.apps.user.models import User
from util.excelUtil import writeExcel
import logging
from django.forms.models import model_to_dict
logger = logging.getLogger(__name__)

class UserModelUtil(ModelUtilAbstract):
    # 不输出的字段
    modelFieldExclude = ['is_superuser', 'is_staff','is_active']
    # 不显示的字段
    modelShowFieldExclude = ['is_superuser', 'is_staff','is_active']
    # 不显示的字段类型
    modelFieldTypeExclude = ['id', 'is_superuser','is_staff','is_active']

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

    def getDatas(self, search_field, current_page, page_size):
        qand = Q()
        if search_field.__len__() != 0:
            for search_key in search_field:
                if search_key == 'groups':
                    useridlist = []
                    for svalue in search_field[search_key]:
                        g = Group.objects.filter(Q(name=svalue)).first()
                        b = g.user_set.all()
                        for user in b:
                            logger.info(user.id)
                            useridlist.append(user.id)
                    qand.add(Q(id__in=useridlist), Q.AND)
                else:
                    qor = Q()
                    qor.connector = Q.OR
                    for svalue in search_field[search_key]:
                        # qor.add(Q(**{skey: svalue.strip()}), Q.OR)
                        qor.children.append((search_key, svalue.strip()))
                    qand.add(qor, Q.AND)
        qand.add(~Q(is_active=0), Q.AND)
        start = (current_page - 1) * page_size
        end = current_page * page_size
        showList = self.getModelShowField()
        dataList = self.modelobj.objects.filter(qand).values(*showList).order_by('id')[start:end]
        data = []
        for item in dataList:
            groups = Group.objects.filter(Q(user=item['id'])).first()
            item['groups'] = groups.name
            data.append(item)
        dataSize = self.modelobj.objects.filter(qand).__len__()
        return data, dataSize

    def getChoicesFieldDict(self):
        choicesFieldDict = {}
        groups = Group.objects.all()
        choicesFieldList=[]
        for item in groups:
            choicesFieldList.append({
                'value': item.name,
                'name': item.name
            })
        choicesFieldDict['groups'] = choicesFieldList
        return choicesFieldDict

    def getModelField(self):
        fileddic = {}
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelFieldExclude]:
            fileddic[i.name] = i.verbose_name
        fileddic['groups'] = '用户组'
        return fileddic

    def getModelFieldType(self):
        fieldType = {}
        choicesFieldList = []
        if hasattr(self.modelobj, 'ChoicesField'):
            ModelChoicesFieldDict = self.modelobj.ChoicesField
            for field in ModelChoicesFieldDict:
                choicesFieldList.append(field)
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelFieldTypeExclude]:
            if i.name in choicesFieldList:
                fieldType[i.name] = 'ChoicesField'
            else:
                fieldType[i.name] = type(i).__name__
        fieldType['groups'] = 'ChoicesField'
        return fieldType

    def getModelShowField(self):
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
        return writeExcel(self.modelName, columnList, datas)

    def addObj(self, data):
        groups = data.pop('groups')
        if groups:
            groups = 'newuser'
        try:
            newUser = self.modelobj.objects.create_user(**data)
            newUser.save()
            g = Group.objects.filter(Q(name=groups)).first()
            newUser.groups.add(g)
        except Exception as e:
            logger.info(e)
            return False
        return True

    def delObj(self, IdList):
        for id in IdList:
            obj = self.modelobj.objects.filter(Q(id=id))[0]
            obj.is_active = 0
            obj.save()

    def updateObj(self, updateData):
        obj = self.modelobj.objects.filter(Q(id=updateData['data']['id']))[0]
        for item in updateData['data']:
            if item != 'username' and item != 'groups':
                setattr(obj, item, updateData['data'][item])
        obj.save()
        obj.groups.remove(Group.objects.filter(Q(user=obj.id)).first())
        obj.groups.add(Group.objects.filter(Q(name=updateData['data']['groups'])).first())
