from django.db import models

# Create your models here.
class Order_Info(models.Model):#主表
    oid =models.CharField(max_length=20,primary_key=True)#订单编号，主键
    user =models.ForeignKey('df_user.UserInfo')#用户
    odate = models.DateTimeField(auto_now=True)#创建时间
    oIspay = models.BooleanField(default=False)#是否支付
    ototal = models.DecimalField(max_digits=6,decimal_places=2)#总金额
    #max_digits表示所有位数的最大位数，decomal_places表示小数位的位数
class Order_DetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    order = models.ForeignKey(Order_Info)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.IntegerField()#数量
