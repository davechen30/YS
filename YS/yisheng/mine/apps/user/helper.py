from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from mine.API.powerOperations.powerOperation import PowerOperation
from mine.apps.component import helper as componentHelper
from .models import User
import json
import logging
# import redis
# from django_redis import get_redis_connection

# mine
from mine.apps.nav.helper import NavHelper

logger = logging.getLogger(__name__)

@ensure_csrf_cookie
def testLogin(request):
    try:
        user = User.objects.filter(Q(username=request.GET['username'])).first()
        if user:
            if user.check_password(request.GET['password']):
                permissionDict = PowerOperation(user).getPermissionDict()
                # logger.info(permissionDict)
                nav,componentSet = NavHelper(user).getNav()
                # logger.info(nav)
                componentList = componentHelper.getComponentList(componentSet)
                routedata = {'routes':nav,'componentList':componentList}
                datas = {'code':1}
                datas['username'] = user.username
                datas['permissionDict'] = json.dumps(permissionDict)
                # logger.info(permissionDict)
                datas['routes'] = json.dumps(routedata)
                logger.info('LoginAction:' + user.username + ' login-------')
                logger.info(datas)
                response = JsonResponse(datas)
            else:
                response = JsonResponse({'code':0,'msg':'username or password error'})
        else:
            response = JsonResponse({'code': 0, 'msg': 'username or password error'})
    except Exception as e:
        logger.info(e)
        response = JsonResponse({'code':0,'msg':'login error'})
    finally:
        return response
