from django.shortcuts import render,redirect
from core.models import *
from core.forms import *
def home(request):
    return render(request,"home.html")
def student_d(request):
    form = addtask()
    if request.method =="POST":
        data=addtask(request.POST)
        if data.is_valid():
            data.save()
            return redirect("home")
        context = {"form":form}
    return render(request,'home', context=context)