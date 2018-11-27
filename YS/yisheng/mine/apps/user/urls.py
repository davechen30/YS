from django.conf.urls import url
from .views import api_root,UserDetail,UserList,PositionDetail,RoelDetail,TokenDetail

urlpatterns = [
    url(r'^$',api_root),
    url(r'^user/$', UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^position/$', PositionDetail.as_view(), name='position-list'),
    url(r'^roel/$', RoelDetail.as_view(), name='role-list'),
    url(r'^token/$', TokenDetail, name='token-list'),
    # url(r'^organizations/$', organization_list, name='organization-list'),
    # url(r'^organizations/(?P<pk>[0-9]+)/$', organization_detail, name='organization-detail'),
    # url(r'^departments/$', department_list, name='department-list'),
    # url(r'^departments/(?P<pk>[0-9]+)/$', department_detail, name='department-detail'),
    # url(r'^positions/$', position_list, name='position-list'),
    # url(r'^positions/(?P<pk>[0-9]+)/$', position_detail, name='position-detail'),

]