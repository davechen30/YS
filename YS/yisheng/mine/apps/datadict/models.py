from django.db import models

# Create your models here.
class DataDict(models.Model):
    name = models.CharField(max_length=50,default=None,null=False,blank=False,unique=True,verbose_name="名字")
    code = models.CharField(default=None,null=False,blank=False,unique=True,verbose_name="编码")
    data = models.CharField(max_length=255,default=None,null=False,blank=False,verbose_name="数据")