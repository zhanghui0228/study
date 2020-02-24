from django.db import models

# Create your models here.

class CommonUtil(models.Model):
    ''' 定义抽象类，用于每个表中有字段重复的 '''
    created_at = models.DateTimeField('创建时间', auto_now_add=True)  # auto_now_add=True, 自动生成创建时间
    updated_at = models.DateTimeField('最后更新时间', auto_now=True)  # auto_now=True, 自动生成更新时间

    class Meta:
        abstract = True     # 抽象类


class Course(CommonUtil):
    ''' 课程表 '''
    name = models.CharField('课程名称', max_length=64)

    class Meta:
        db_table = 'course'
        verbose_name = '课程表信息'


class Student(CommonUtil):
    ''' 学生表 '''
    name = models.CharField(max_length=64, verbose_name='姓名')
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '男'),
        ('0', '女'),
    ))
    age = models.PositiveIntegerField('年龄')     # 只能为正整数
    username = models.CharField('登录名', max_length=64, unique=True)      # unique=True, 表示唯一，不能有重复
    password = models.CharField('密码', max_length=256)
    # created_at = models.DateTimeField('创建时间', auto_now_add=True)     # auto_now_add=True, 自动生成创建时间
    # updated_at = models.DateTimeField('最后更新时间', auto_now=True)         # auto_now=True, 自动生成更新时间
    courses = models.ManyToManyField(Course)    # 外键关联，多对多

    # 内部类
    class Meta:
        db_table = 'students'
        verbose_name = '学生表基本信息'
        ordering = ['-updated_at']      # 降序排序

    # def get_name(self):
    #     # 返回学生的姓
    #     return self.name[0]


class UserDatil(models.Model):
    ''' 用户详细信息表， 实现一对一关系'''
    students = models.OneToOneField(Student)    # 外键关联，一对一关系 （一个学生对应其一个座右铭）
    sign = models.CharField('座右铭', max_length=256)


class UserAddr(CommonUtil):
    ''' 用户的地址 实现一对多关系 '''
    useraddrees = models.ForeignKey(Student)    # 外键关联， 一对多关系（一个学生对应多个地址）
    phone = models.IntegerField('电话', max_length=11)
    address = models.CharField('地址', max_length=256)
    is_valid = models.BooleanField('受否有效', default=True)

    class Meta:
        db_table = 'address'