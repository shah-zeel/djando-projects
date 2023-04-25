from django.urls import path
from .views import TaskList, TaskDetail     # '.' bez they are in the same file structure

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]