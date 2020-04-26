from django.db import models

# Create your models here.
'''
    模型：
    student_name    学生姓名
    subject_name    科目名称
    score           成绩
    year            学期
'''

class Grade(models.Model):
    """ 学生成绩表 """
    student_name = models.CharField("学生姓名", max_length=32)
    subject_name = models.CharField("科目", max_length=32)
    score = models.FloatField('分数', default=0)
    year = models.SmallIntegerField('年份')

    class Meta:
        db_table = 'grade'