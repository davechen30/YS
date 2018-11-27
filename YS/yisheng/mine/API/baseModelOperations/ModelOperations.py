import io
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from mine.API.baseModelOperations.modelUtilFactory import modelUtilFactory
from mine.apps.user.models import User

logger = logging.getLogger(__name__)

# 获取数据
@csrf_exempt
def getMsg(request):
    '''
    :param request:
     modelName model的名
     current_page 第几页
     page_size 每页多少条数据
     search_field  查询条件
    :return:
    data 搜索数据
    column 列名
    dataSize 数据大小
    fieldType 字段类型
    choicesFieldDict 下拉选项字典的字典
    '''
    modelName = request.GET['model']
    current_page = int(request.GET['current_page'])
    page_size = int(request.GET['page_size'])
    search_field = json.loads(request.GET['search_field'])
    datas = modelUtilFactory().getModelUtil(modelName).getPostData(search_field,current_page,page_size)
    return JsonResponse(datas)

# 添加数据
@csrf_exempt
def addMsg(request):
    modelName = request.GET['model']
    data = json.loads(request.GET['data'])
    if modelUtilFactory().getModelUtil(modelName).addObj(data):
        return JsonResponse({'msg':'succeed','code':1})
    return JsonResponse({'msg':'error','code':0})

# 删除数据
@csrf_exempt
def delMsg(request):
    modelName = request.GET['model']
    IdList = json.loads(request.GET['keys'])
    modelUtilFactory().getModelUtil(modelName).delObj(IdList)
    return JsonResponse({'msg':'succeed','code':1})

# 更新数据
@csrf_exempt
def updateMsg(request):
    '''
    update data list
    '''
    modelName = request.GET['model']
    datas = json.loads(request.GET['datas'])
    modelUtilFactory().getModelUtil(modelName).updateObj(datas)
    return JsonResponse({'msg':"update succeed",'code': 1})


@csrf_exempt
def downloadExcel(request):
    modelName = request.GET['model']
    file = modelUtilFactory().getModelUtil(modelName).downloadModelExcel()
    # file = open("E://hi.xls",'rb')
    sio = io.BytesIO()
    file.save(sio)
    # file.save("E://hi.xls")
    # logger.info(type(file))
    sio.seek(0)
    logger.info(type(sio.getvalue()))
    response = HttpResponse(sio.getvalue(), content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment;filename=test.xlsx'
    response.write(sio.getvalue())
    return response