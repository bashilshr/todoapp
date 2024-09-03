
from core.forms import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.models import task
class tasklist (ListView):
    model = task
    context_object_name = 'tasks'
    template_name = "task_list.html"
class taskdetail (DetailView):
    model = task
    context_object_name = 'task'
    template_name = "task_detail.html"

class taskcreate (CreateView):
    model = task
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = "task_form.html"