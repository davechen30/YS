from django.conf.urls import url
from mine.API.baseModelOperations import ModelOperations

urlpatterns = [
    # modelCRUD
    url(r'^getMsg$', ModelOperations.getMsg, name='getMsg'),
    url(r'^addMsg$', ModelOperations.addMsg, name='addMsg'),
    url(r'^delMsg$', ModelOperations.delMsg, name='delMsg'),
    url(r'^updateMsg$', ModelOperations.updateMsg, name='updateMsg'),
    url(r'^downloadExcel$', ModelOperations.downloadExcel, name='downloadExcel'),
]