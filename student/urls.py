from django.urls import path, include

from student.views import routing_logic
from . import views


app_name = 'student'
urlpatterns = [
    path('',routing_logic, name = 'route'),
    path('home/', views.student_dashboard, name='student_dashboard'),
    path('profile/', views.student_profile, name='student_profile'),
    path('budget/', include('budget.urls'), name='student_budget'),
    # todo : Niharika, dolby will do the budget above

    path('project_details/', views.student_project_details, name='student_project_details'),
    path('completion_report/', views.student_completion_report, name='student_completion_report'),

]
