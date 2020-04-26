from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum, Max, Min, Avg

# Create your views here.
from  student.models import Grade

# 聚合及统计
def page_stas(request):
    """ 聚合及统计 """
    # 使用aggregate
    # 计算user4成绩总和
    # grade_list = Grade.objects.filter(student_name='user4').aggregate(Sum('score'))
    grade_list = Grade.objects.filter(student_name='user4').aggregate(总成绩=Sum('score'))
    print(grade_list)

    # 计算 A 科目的最高分
    grade_A_high = Grade.objects.filter(subject_name='A').aggregate(最高分=Max('score'))
    print(grade_A_high)

    # 计算 B 科目的最低分
    grade_B_min = Grade.objects.filter(subject_name='B').aggregate(最低分=Min('score'))
    print(grade_B_min)

    # 计算 A 科目的平均分
    grade_A_avg = Grade.objects.filter(subject_name='A').aggregate(平均分=Avg('score'))
    print("A 科目的平均分：{}".format(grade_A_avg['平均分']))

    # 使用annotate
    # 求每个学生的成绩总和
    every_list = Grade.objects.values_list('student_name').annotate(Sum('score'))
    for item in every_list:
        print(item)
    return HttpResponse('OK')