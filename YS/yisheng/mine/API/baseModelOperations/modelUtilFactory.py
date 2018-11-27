from mine.API.baseModelOperations.modelUtil.basicModelUtil import BasicModelUtil
from mine.API.baseModelOperations.modelUtil.groupsModelUtil import GroupsModelUtil
from mine.API.baseModelOperations.modelUtil.userModelUtil import UserModelUtil
from mine.API.baseModelOperations.modelUtil.permissionModelUtil import PermissionModelUtil

import logging

logger = logging.getLogger(__name__)

class modelUtilFactory:

    def getModelUtil(self,model):
        return {
            'user_User': UserModelUtil(model),
            'auth_Permission': PermissionModelUtil(model),
            'auth_Group': GroupsModelUtil(model),
        }.get(model,BasicModelUtil(model))
