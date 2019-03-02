from django.shortcuts import render

# Create your views here.


def guide_dashboard(request):

    return render(request,'guide_dashboard/guide_dashboard.html')

def guide_profile(request):
    return render(request,'guide_dashboard/guide_profile.html')

def guide_student(request):
    request.user

    return render(request,'guide_dashboard/guide_student.html')

