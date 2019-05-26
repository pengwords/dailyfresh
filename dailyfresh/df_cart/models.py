from django.db import models
from df_goods.models import GoodsInfo
from df_user.models import UserInfo
# Create your models here.


class CartInfo(models.Model):
    user = models.ForeignKey(
        'df_user.UserInfo',
        on_delete=models.CASCADE)  # 购买者
    goods = models.ForeignKey(
        'df_goods.GoodsInfo',
        on_delete=models.CASCADE)  # 购买的商品
    count = models.IntegerField()  # 够买数量
