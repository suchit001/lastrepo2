from django.shortcuts import render

from project.models import project_details
from .models import sec_details
from users.models import CustomUser

# Create your views here.


def secretariat_dashboard(request):
    return render(request,'secretariat_dashboard/sec_dashboard.html')

def secretariat_profile(request,):
    sec = sec_details.objects.filter(sec_id__in = CustomUser.objects.filter(username = request.user.username))
    #sec = sec_details.objects.all()
    print(sec)
    sec = sec[0]
    context = {
        'sec' : sec
    }
    return render(request,'secretariat_dashboard/sec_profile.html',context)

def secretariat_director_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_director_review.html',context)

def secretariat_irb_review(request):
    return render(request,'secretariat_dashboard/sec_irb_review.html')

def secretariat_final_review(request):
    return render(request,'secretariat_dashboard/sec_final_review.html')