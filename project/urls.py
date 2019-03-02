from django.urls import path

from project.views import display_form1

app_name = 'project'

urlpatterns = [
    path('', display_form1,name= 'project'),
]
