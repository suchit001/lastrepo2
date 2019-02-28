from django.shortcuts import render

# Create your views here.


def secretariat_dashboard(request):
    return render(request,'secretariat_dashboard/sec_dashboard.html')

def secretariat_profile(request):
    return render(request,'secretariat_dashboard/sec_profile.html')

def secretariat_director_review(request):
    return render(request,'secretariat_dashboard/sec_director_review.html')

def secretariat_irb_review(request):
    return render(request,'secretariat_dashboard/sec_irb_review.html')

def secretariat_final_review(request):
    return render(request,'secretariat_dashboard/sec_final_review.html')
