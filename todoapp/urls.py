from django.contrib import admin
from django.urls import path
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tasklist.as_view(), name = "tasks"),
    path('task/<int:pk>/',taskdetail.as_view(), name = "task"),
        path('task-create',taskcreate.as_view(), name = "task-create"),

    

]
