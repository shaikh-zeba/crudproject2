from django import forms 
from.models import *

class StudenttForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        
class CollegeeForm(forms.ModelForm):
    class Meta:
        model=College
        fields="__all__"                 