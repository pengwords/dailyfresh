from .models import GoodsInfo
from haystack import  indexes


class GoodsInfoIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)
    #对标题，简介，内容进行搜索
    gtitle= indexes.CharField(model_attr='gtitle')
    gjianjie = indexes.CharField(model_attr='gjianjie')
    gcontent = indexes.CharField(model_attr='gcontent')


    def get_model(self):
        return  GoodsInfo


    def index_queryset(self, using=None):
        return self.get_model().objects.all()
    #每个索引里面必须有且只能有一个字段document=True