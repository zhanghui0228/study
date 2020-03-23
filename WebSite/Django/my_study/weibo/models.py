from django.db import models

# Create your models here.


class WeiboUser(models.Model):
    """ 微博用户 """
    username = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('昵称', max_length=32)

    class Meta:
        db_table = 'weibo_user'


class WeiBo(models.Model):
    """ 微博 """
    context = models.CharField('微博内容', max_length=500)
    user = models.ForeignKey(WeiboUser, verbose_name='用户')    # 关联WeiboUser表中的用户
    create_at = models.DateTimeField('发布时间', auto_now_add=True)     # 自动填写创建发布时间
    source = models.CharField('发布来源', null=True, blank=True, max_length=20)     # 可以为空值

    class Meta:
        db_table = 'weibo'


class WeiboImage(models.Model):
    """ 微博图片 """
    weibo = models.ForeignKey(WeiBo, verbose_name='关联微博')
    image = models.ImageField(upload_to='images/weibo', verbose_name='图片')

    class Meta:
        db_table = 'weibo_image'


class Comment(models.Model):
    """ 微博评论 """
    context = models.CharField('评论内容', max_length=256)
    create_at = models.DateTimeField('评论时间', auto_now_add=True)
    user = models.ForeignKey(WeiboUser, verbose_name="评论用户")
    weibo = models.ForeignKey(WeiBo, verbose_name='评论微博')

    class Meta:
        db_table = 'weibo_comment'


class Friend(models.Model):
    """ 用户与用户关系 """
    user_from = models.ForeignKey(WeiboUser, verbose_name='关注用户', related_name='user_from')
    user_to = models.ForeignKey(WeiboUser, verbose_name='被关注用户', related_name='user_to')
    create_at = models.DateTimeField('关注时间', auto_now_add=True)

    class Meta:
        db_table = 'weibo_friend'