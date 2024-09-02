from core.models import *
from django import forms
class addtask(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'