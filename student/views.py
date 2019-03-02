from django.shortcuts import render, redirect

# Create your views here.
from student.models import Std_details
from users.models import CustomUser


def routing_logic(request):
    student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    student = student[0]
    if(student.st_project_status==0):
        return redirect('project:project')
    else:
        return redirect('student:student_dashboard')


def student_dashboard(request):
    #student = Std_details.objects.filter(student_id__in=CustomUser.objects.filter(username=str(request.user.username)))
    # guidename = Director_details.objects.filter(principal_id__in=CustomUser.objects.filter(username=student[0].guide))
    # print(student[0].student_id)
    # context= {
    #     'student': student[0],
    #     'guide': guidename[0],
    # }
    return render(request,'student_dashboard/student_dashboard.html')

def student_profile(request):
    return render(request,'student_dashboard/student_profile.html')

def student_budget(request):
    return render(request,'student_dashboard/student_budget.html')

def student_project_details(request):
    return render(request,'student_dashboard/student_project_details.html')

def student_completion_report(request):
    return render(request,'student_dashboard/student_completion_report.html')
