from django.contrib import admin

from secretariat.models import sec_details
from student.models import Std_details

admin.site.register(sec_details)

admin.site.register(Std_details)