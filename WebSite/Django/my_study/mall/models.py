from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from accounts.models import Student


class Product(models.Model):
    ''' 商品表 '''
    name = models.CharField('商品名称', max_length=64)
    # 反向关联（查看商品被多少人收藏）
    collections = GenericRelation('Collection')     # 反向关联


class Store(models.Model):
    ''' 店铺表 '''
    name = models.CharField('店铺名称', max_length=64)


class Collection(models.Model):
    ''' 收藏表 '''
    user = models.ForeignKey(Student)       # 关联accounts上的 Student模块表中的用户
    content_type = models.ForeignKey(ContentType)       # 关联模型
    object_id = models.IntegerField('关联的ID')
    content_object = GenericForeignKey('content_type', 'object_id')     # 关联模型对象
    create_at = models.DateTimeField('收藏时间', auto_now_add=True)     # 收藏时间