from core.models import *
from django import forms
class addStudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
