from django.shortcuts import render

# Create your views here.


def director_dashboard(request):
    return render(request,'director_dashboard/director_dashboard.html')

def director_profile(request):
    return render(request,'director_dashboard/director_profile.html')

def director_student_details(request):
    return render(request,'director_dashboard/director_student_details.html')

def director_project_details(request):
    return render(request,'director_dashboard/director_project_details.html')

def director_guide_details(request):
    return render(request,'director_dashboard/director_guide_details.html')

def director_secretariat_details(request):
    return render(request,'director_dashboard/director_secretariat_details.html')
