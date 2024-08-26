from django.shortcuts import render,redirect
from core.models import *
from core.forms import *
def home(request):
    return render(request,"home.html")
def student_d(request):
    form = addStudentForm()
    if request.method =="post":
        data=addStudentForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect("home")
        context = {"form":form}
    return render(request,'home', context=context)