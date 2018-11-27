from django.conf.urls import url

from .loginOperations import testLogin
urlpatterns = [
    # modelCRUD
    url(r'^testlogin/',testLogin,name='testLogin'),
]