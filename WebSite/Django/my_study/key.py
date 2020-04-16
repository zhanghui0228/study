# 有外键关联的数据创建
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')
django.setup()
from weibo.models import WeiboUser
from  weibo.models import WeiBo
from  weibo.models import Comment

# zhangsan = WeiboUser.objects.get(username='zhangsan')   # 用户
# weibo = WeiBo.objects.create(user=zhangsan, context="this is foreignkey create test")   # 微博内容
# comment = Comment.objects.create(user=zhangsan, context="this is comment", weibo=weibo)  # 评论

user1 = WeiboUser.objects.get(username='user1')
user1_weibo = WeiBo.objects.create(user=user1, context='my is user1')
user1_comment = Comment.objects.create(user=user1, context='user1 is comment', weibo=user1_weibo)