from django.shortcuts import render,redirect
from core.models import *
from core.forms import *
from django.views.generic.list import ListView
class tasklist (ListView):
    quweryset = task.objects.all()
class taskdetail (ListView):
    quweryset = task.objects.all()