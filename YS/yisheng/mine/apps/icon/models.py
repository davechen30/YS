from django.db import models

# Create your models here.
class Icon(models.Model):

    name = models.CharField(max_length=50,null=False,blank=False,default=None,verbose_name="图标名")
    iconcode = models.CharField(max_length=50,null=False,blank=False,default=None,verbose_name="图标")

    class Meta:
        verbose_name = "图标"
        verbose_name_plural = verbose_name