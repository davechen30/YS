from django.db import models

# Create your models here.
# NavPower ButtonPower NavItem
class NavItem(models.Model):
    name = models.CharField(max_length=20,null=False,blank=False,verbose_name='菜单名')
    code = models.CharField(max_length=255,null=False,blank=False,verbose_name='菜单编码')
    content_type_id = models.IntegerField(default=0,null=False,blank=False,verbose_name='模块ID')
    is_root = models.BooleanField(default=False,verbose_name='是否为根目录')
    father_code = models.CharField(max_length=255,default=None,null=True,blank=True,verbose_name='父节点')
    has_children = models.BooleanField(default=False,verbose_name='是否有子节点')
    href = models.CharField(max_length=255,default=None,null=True,blank=True,verbose_name='菜单路径')
    icon = models.CharField(max_length=255,default=None,null=True,blank=True,verbose_name='菜单图标')
    component = models.CharField(max_length=255,default='baseType',null=False,blank=False,verbose_name='组件类型')
    status = models.BooleanField(default=True,verbose_name='状态')

    class Meta:
        verbose_name = '菜单项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    ChoicesField = {
        'father_code': {
            'model': 'nav_NavItem',
            'field': 'code',
        },
        'component': {
            'model': 'component_Component',
            'field': 'code',
        },
    }
