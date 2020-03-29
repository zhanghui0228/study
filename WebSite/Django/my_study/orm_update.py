# orm修改操作
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')
django.setup()

from weibo.models import WeiboUser as user

# 方法一：使用模型save()进行修改数据
# user_A = user.objects.get(username='admin')
# user_A.nickname = 'test'
# user_A.save()
# print(user_A.id)

# 方法二： 使用模型update()进行批量修改数据
user_list = user.objects.all()      # 获取所有数据
user_list.update(password='123123')     # 进行批量修改