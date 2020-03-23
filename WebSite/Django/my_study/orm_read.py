# orm查询操作
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')
django.setup()


from weibo.models import WeiboUser as user

# 使用get()查询单条数据
admin = user.objects.get(username='user01')
print("id: {id},username={username},password={password},nickname={nickname}".format(id=admin.pk,
                                                                                    username=admin.username,
                                                                                    password=admin.password,
                                                                                    nickname=admin.nickname))

# 使用all()查询所有数据
all_info = user.objects.all()
# 获取所有用户名
for name in all_info:
    print(name.username)