from django.contrib import admin
from django.urls import path, include

from .views import routing_logic

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('student/', include('student.urls')),
    path('guide/', include('guide.urls')),
    path('director/', include('director.urls')),
    path('secretariat/', include('secretariat.urls')),

    path('users/', include('django.contrib.auth.urls')),
    path('', routing_logic, name='routing_logic'),

]
