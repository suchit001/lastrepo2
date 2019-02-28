from django.urls import path
from . import views


app_name = 'student'
urlpatterns = [
    path('student/home/', views.student_dashboard, name='student_dashboard'),
    path('student/profile/', views.student_profile, name='student_profile'),
    # path('student/budget/', views.sample_create_view, name='student_budget'),
    # todo : Niharika, dolby will do the budget above

    path('student/project_details/', views.student_project_details, name='student_project_details'),
    path('student/completion_report/', views.student_completion_report, name='student_completion_report'),
]
