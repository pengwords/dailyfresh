from django.db import models

# Create your models here.


class Order_Info(models.Model):  # 主表
    oid = models.CharField(max_length=20, primary_key=True)  # 订单编号，主键
    user = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)  # 用户
    odate = models.DateTimeField(auto_now=True)  # 创建时间
    oIspay = models.BooleanField(default=False)  # 是否支付
    ototal = models.DecimalField(max_digits=6, decimal_places=2)  # 总金额
    oaddress=models.CharField(max_length=100)#收货地址
    # max_digits表示所有位数的最大位数，decomal_places表示小数位的位数
#无法实现 真实支付，物流信息（要调用对应接口)

class Order_DetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)  # 关联商品表
    order = models.ForeignKey(Order_Info,on_delete=models.CASCADE)  # 关联订单表
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 商品价格
    count = models.IntegerField()  # 商品数量
