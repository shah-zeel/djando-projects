from django.urls import path
from . import views     # '.' bez they are in the same file structure

urlpatterns = [
    path('', views.taskList, name='tasks'),
]