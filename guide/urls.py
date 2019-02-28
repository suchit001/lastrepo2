from django.urls import path
from . import views
app_name = 'guide'

urlpatterns = [
    path('guide/home/', views.guide_dashboard, name='guide_dashboard'),
    path('guide/profile/', views.guide_profile, name='guide_profile'),
    path('guide/student/', views.guide_student, name='guide_student'),
]
