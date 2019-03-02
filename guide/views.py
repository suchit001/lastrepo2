from django.shortcuts import render

# Create your views here.
from guide.models import Principal_investigator
from project.models import project_details


def guide_dashboard(request):

    return render(request,'guide_dashboard/guide_dashboard.html')

def guide_profile(request):
    return render(request,'guide_dashboard/guide_profile.html')

def guide_student(request):
    g1=Principal_investigator.objects.get(principal_id=request.user)
    g2=project_details.objects.filter(PI_id=g1)

    context={
        "project":g2
    }

    return render(request,'guide_dashboard/guide_student.html',context)

