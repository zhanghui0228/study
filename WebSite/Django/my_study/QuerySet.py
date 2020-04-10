# 结果集QuerySet的使用
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')
django.setup()

from weibo.models import WeiboUser as user

# 使用get_or_create()
user_obj = user.objects.get_or_create(username="zhangsan", password='123123', nickname='zs')
# print(user_obj[0])
print(user_obj)

# 使用bulk_create() 批量创建多条记录
# user1 = user(username='user1', nickname='01', password='123123')
# user2 = user(username='user2', nickname='02', password='123123')
# user3 = user(username='user3', nickname='03', password='123123')
# user_list = [user1, user2, user3]
# create_many_user = user.objects.bulk_create(user_list)
# print(create_many_user)

# first/last() 查询第一条/最后一条记录
user_first = user.objects.first()   # 返回第一条数据
user_last = user.objects.last()     # 返回最后一条数据
print(user_first.username)
print(user_last.nickname)

# 使用count() 返回数据的行数之和
user_all = user.objects.all()
user_count = user_all.count()
print(user_count)

# 使用exists() 判断结果集是否存在
use = user.objects.filter(username='zhangsan').exists()
use1 = user.objects.filter(username='lisi').exists()
print(use, use1)
print("------------------------------------------")

# 对QuerySet进行分片实现分页
limit = user.objects.all()
page = limit[1:5]
for i in page:
    print(i.username, i.nickname)