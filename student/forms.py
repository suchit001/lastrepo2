from django import forms
from .models import *

class research_fellow_form(forms.ModelForm):
    class Meta:
        model = Std_details
        fields = [ 'st_designation']
        labels = {'st_designation': 'Designation',}

class student_details_form(forms.ModelForm):
    class Meta:
        model = Std_details
        fields = ['st_study_purpose', 'st_study_other','st_any_pub']
        labels = {'st_study_purpose':'Select Study Purpose','st_study_other':'Others (Specify)',
                  'st_any_pub':'Any Publications or work in the field of the Study,(not necessarily restricted to the present study) by investigator'}
