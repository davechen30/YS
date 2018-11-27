from django.contrib.auth.models import Group, Permission
from django.db.models import Q

from mine.API.baseModelOperations.modelUtil.ModelUtilAbstract import ModelUtilAbstract
from util.excelUtil import writeExcel
import logging
from django.forms.models import model_to_dict
logger = logging.getLogger(__name__)

class GroupsModelUtil(ModelUtilAbstract):
    ORDER_BY = 'id'
    # 不输出的字段
    modelFieldExclude = []
    # 不显示的字段
    modelShowFieldExclude = []
    # 不显示的字段类型
    modelFieldTypeExclude = []

    Excule = ['add_logentry',
              'delete_logentry',
              'view_logentry',
              'change_logentry',
              'add_token',
              'change_token',
              'delete_token',
              'view_token',
              'add_contenttype',
              'change_contenttype',
              'delete_contenttype',
              'view_contenttype',
              'add_revision',
              'change_revision',
              'delete_revision',
              'view_revision',
              'add_version',
              'change_version',
              'delete_version',
              'view_version',
              'add_session',
              'change_session',
              'delete_session',
              'view_session',
              'add_token',
              'change_token',
              'delete_token',
              'view_token',
              'add_bookmark',
              'change_bookmark',
              'delete_bookmark',
              'view_bookmark',
              'add_log',
              'change_log',
              'delete_log',
              'view_log',
              'add_usersettings',
              'change_usersettings',
              'delete_usersettings',
              'view_usersettings',
              'add_userwidget',
              'change_userwidget',
              'delete_userwidget',
              'view_userwidget']

    def getPostData(self,search_field, current_page, page_size):
        q = self._generateQ(search_field)
        self.generatePermissionList()
        datas = {}
        datas['data'] = self.getDatas(q, current_page, page_size)
        datas['column'] = self.getModelField()
        datas['dataSize'] = self._getDataSize(q)
        datas['fieldType'] = self.getModelFieldType()
        datas['choicesFieldDict'] = self.getChoicesFieldDict()
        datas['permissionslist'] = self.generatePermissionList()
        return datas

    def getDatas(self,qand,current_page,page_size):
        start = (current_page - 1) * page_size
        end = current_page * page_size
        data = []
        dataList = self.modelobj.objects.filter(qand).values(*self.getModelShowField()).order_by(self.ORDER_BY)[start:end]
        for item in dataList:
            group = Group.objects.filter(Q(id=item['id'])).first()
            permissions = []
            for permission in group.permissions.all().order_by('id'):
                obj = model_to_dict(permission)
                permissions.append(obj['id'])
            item['permissions'] = permissions
            item['showpermissions'] = self.generateGroupsPermissionList(group)
            data.append(item)
        return data

    def generatePermissionList(self):
        permissionList = []
        index = 0
        navitemcache = {}
        for a in Permission.objects.all():
            if a.codename in self.Excule:
                continue
            navitem = a.name.split(' ',2)[2]
            if navitem not in navitemcache:
                navitemcache[navitem] = index
                index += 1
                permissionList.append({
                    'label': navitem,
                    'children': [{
                        'id':a.id,
                        'label':a.name
                    }]
                })
            else:
                permissionList[navitemcache[navitem]]['children'].append({
                    'id':a.id,
                    'label':a.name
                })
        return permissionList

    def generateGroupsPermissionList(self,group):
        permissionList = []
        index = 0
        navitemcache = {}
        for a in group.permissions.all().order_by('id'):
            if a.codename in self.Excule:
                continue
            navitem = a.name.split(' ',2)[2]
            if navitem not in navitemcache:
                navitemcache[navitem] = index
                index += 1
                permissionList.append({
                    'label': navitem,
                    'children': [{
                        'id':a.id,
                        'label':a.name
                    }]
                })
            else:
                permissionList[navitemcache[navitem]]['children'].append({
                    'id':a.id,
                    'label':a.name
                })
        return permissionList

    def _generateQ(self,search_field):
        qand = Q()
        if (search_field.__len__() != 0):
            for search_key in search_field:
                qor = Q()
                qor.connector = Q.OR
                for svalue in search_field[search_key]:
                    # qor.add(Q(**{skey: svalue.strip()}), Q.OR)
                    qor.children.append((search_key, svalue.strip()))
                qand.add(qor, Q.AND)
        if (self.modelName == 'User') & (self.appName == 'user'):
            qand.add(~Q(is_active=0), Q.AND)
        else:
            if self.appName != 'auth':
                qand.add(~Q(status=0), Q.AND)
        return qand

    def _getDataSize(self,q):
        return self.modelobj.objects.filter(q).__len__()

    def getModelField(self):
        fileddic = {}
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelFieldExclude]:
            fileddic[i.name] = i.verbose_name
        return fileddic

    def getModelFieldType(self):
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
        filedList = []
        filed = self.modelobj._meta.fields
        for i in [j for j in filed if j.name not in self.modelShowFieldExclude]:
            filedList.append(i.name)
        return filedList

    def addObj(self,data):
        try:
            self.modelobj.objects.create(**data)
        except Exception as e:
            logger.info(e)
            return False
        return True

    def delObj(self,IdList):
        for id in IdList:
            self.modelobj.objects.filter(Q(id=id)).delete()


    def updateObj(self,updateData):
        logger.info(updateData)
        if 'newPermissions' in updateData:
            logger.info("has")
            obj = self.modelobj.objects.filter(Q(id=updateData['data']['id']))[0]
            obj.permissions.clear()
            logger.info(obj.permissions.all())
            for id in updateData['newPermissions']:
                obj.permissions.add(Permission.objects.filter(Q(id=id)).first())
            logger.info(obj.permissions.all())
        else:
            obj = self.modelobj.objects.filter(Q(id=updateData['data']['id']))[0]
            for item in updateData['data']:
                setattr(obj, item, updateData['data'][item])
            obj.save()