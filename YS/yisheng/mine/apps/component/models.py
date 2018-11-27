from django.db import models

# Create your models here.
class Component(models.Model):

    name = models.CharField(max_length=255,default=None,null=False,blank=False,verbose_name='组件名')
    code = models.CharField(max_length=255,default=None,null=False,blank=False,verbose_name='编码')
    path = models.CharField(max_length=255,default=None,null=False,blank=False,verbose_name='路径')
    status = models.BooleanField(default=True,verbose_name='状态')

