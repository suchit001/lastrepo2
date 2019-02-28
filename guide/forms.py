from django import forms
from .models import *

class princi_form(forms.ModelForm):
    class Meta:
        model = Principal_investigator
        fields = ['P_designation','P_Dept']
        labels ={
            'P_designation':'Designation',
            'P_Dept':'Department',
        }

class coinv_form(forms.ModelForm):
    class Meta:
        model = Co_Investigator
        fields = ['Co_designation']
        labels = {'Co_designation': 'Designation'}
