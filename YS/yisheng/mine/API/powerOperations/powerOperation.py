

from django.contrib.auth.models import Permission, _user_get_all_permissions


class PowerOperation:

    def __init__(self,user):
        self.user = user

    def getPermissionDict(self):
        permissionDict = {}
        appmodelset = set()
        excule = ['xadmin_userwidget',
                  'sessions_session',
                  'xadmin_log',
                  'user_token',
                  'reversion_revision',
                  'xadmin_bookmark',
                  'admin_logentry',
                  'xadmin_usersettings',
                  'contenttypes_contenttype',
                  'authtoken_token',
                  'reversion_version']
        for item in self.user.get_all_permissions():
            '''
            item格式为:
                appname.operationname_modelname
            '''
            appname = item.split('.', 1)[0]
            operationname,modelname = item.split('.', 1)[1].split('_',1)
            appmodel = appname+'_'+modelname
            if appmodel in excule:
                continue
            if appmodel in appmodelset:
                permissionDict[appname + '_' + modelname][operationname] = True
            else:
                appmodelset.add(appmodel)
                permissionDict[appname + '_' + modelname] = {operationname:True}
        # 'auth_permission': {'view': True},
        return permissionDict

    def getNavPermission(self):
        excule = ['xadmin_userwidget',
                  'sessions_session',
                  'xadmin_log',
                  'user_token',
                  'reversion_revision',
                  'xadmin_bookmark',
                  'admin_logentry',
                  'xadmin_usersettings',
                  'contenttypes_contenttype',
                  'authtoken_token',
                  'reversion_version']
        navSet = set()
        for item in self.user.get_all_permissions():
            operationname,modelname = item.split('.', 1)[1].split('_',1)
            if operationname == 'view':
                appname = item.split('.', 1)[0]
                appmodel = appname + '_' + modelname

                if appmodel in excule:
                    continue
                navSet.add(appmodel)
        return list(navSet)