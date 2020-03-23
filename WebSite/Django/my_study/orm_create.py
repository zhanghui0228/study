# ORM新增操作
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')
django.setup()
from weibo.models import WeiboUser as user

# 方法一:
# user_A = user(username='user01', password='admin@123', nickname='admin')
# user_A.save()
# print(user_A.id)

# 方法二：使用模型的create()进行新增数据
user_B = user.objects.create(username='user05', password='admin@123', nickname='user02')
print(user_B.pk)