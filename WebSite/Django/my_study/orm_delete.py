# orm删除操作
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')
django.setup()

from weibo.models import WeiboUser as user

# 使用ORM模型delete()删除单条数据
# user_obj = user.objects.get(username='user001')
# user_obj.delete()

# 使用ORM模型delete()删除多条数据
user_list = user.objects.all()
user_list.delete()