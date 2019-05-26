from django.db import models
from tinymce.models import HTMLField
#富文本编辑器
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


    def __str__(self):
        return  self.ttitle

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)#最多5位，小数位默认两位
    idDelete = models.BooleanField(default=False)
    gunit=models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()#人气
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()#库存
    gcontent = HTMLField()    #使用富文本编辑器
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE) #外键
    gadv = models.BooleanField(default=False)#默认不推荐


    def __str__(self):
        return  self.gtitle

