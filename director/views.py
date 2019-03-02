from django.shortcuts import render

from project.models import project_details
from .models import Director_details
from secretariat.models import sec_details
from guide.models import  Co_Investigator,Principal_investigator
from users.models import CustomUser

# Create your views here.

def director_dashboard(request):
    return render(request,'director_dashboard/director_dashboard.html')

def director_profile(request):
    dir = Director_details.objects.filter(director_id__in=CustomUser.objects.filter(username=request.user.username))
    print(dir)
    dir = dir[0]
    context = {
        'dir': dir
    }
    return render(request,'director_dashboard/director_profile.html',context)

def director_student_details(request):
    return render(request,'director_dashboard/director_student_details.html')

def director_project_details(request):
    project = project_details.objects.all()
    context = {
        'project': project,
    }
    return render(request,'director_dashboard/director_project_details.html',context)


def director_guide_details(request):
    pi = Principal_investigator.objects.all()
    coi = Co_Investigator.objects.all()
    context = {
        'pi' : pi,
    }
    return render(request,'director_dashboard/director_guide_details.html',context)

def director_secretariat_details(request):
    sec = sec_details.objects.all()
    context = {
        'sec': sec
    }
    return render(request,'director_dashboard/director_secretariat_details.html',context)