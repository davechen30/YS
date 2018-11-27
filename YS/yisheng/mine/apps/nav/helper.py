from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import json
import logging

# mine
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from mine.API.powerOperations.powerOperation import PowerOperation
from .models import *

logger = logging.getLogger(__name__)

class NavHelper:

    def __init__(self,user):
        self.user = user

    def getNav(self):
        navlist = []
        fatherSet = set()
        appmodelSet = set()
        excule = ['xadmin_userwidget',
                  'sessions_session',
                  'xadmin_log',
                  'user_token',
                  'reversion_version',
                  'xadmin_bookmark',
                  'admin_logentry',
                  'xadmin_usersettings',
                  'contenttypes_contenttype',
                  'authtoken_token',
                  'reversion_revision']
        li = PowerOperation(self.user).getNavPermission()
        for appmodel in li:
            if appmodel in excule:
                continue
            if appmodel in appmodelSet:
                continue
            appmodelSet.add(appmodel)
            item = NavItem.objects.filter(Q(code=appmodel)).first()
            if item.is_root is False:
                if item.father_code not in fatherSet:
                    fatherSet.add(item.father_code)
                    navlist.append(model_to_dict(NavItem.objects.filter(Q(code=item.father_code))[0]))
            navlist.append(model_to_dict(item))
        componentSet = set()
        for i in navlist:
            if i['component'] != '':
                componentSet.add(i['component'])
        return navlist,componentSet