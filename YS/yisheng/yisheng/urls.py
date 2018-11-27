"""yisheng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
import xadmin

urlpatterns = [
    url(r'^admin/',xadmin.site.urls),#添加新路由
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/', include('mine.apps.user.urls')),
    url(r'^nav/', include('mine.apps.nav.urls')),
    url(r'^modeloperations/', include('mine.API.baseModelOperations.urls')),
    url(r'^yisheng/', include('mine.API.loginOperations.urls')),
]
