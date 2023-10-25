from django import forms 
from .models import User

class StudentRegisteration(forms.ModelForm):
    class Meta:
      model = User
      fields = ['name','rollno','email','password']
      widgets = {
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'rollno':forms.NumberInput(attrs={'class':'form-control'}),
          'email':forms.EmailInput(attrs={'class':'form-control'}),
          'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
          
          }
    