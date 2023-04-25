from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate     # '.' bez they are in the same file structure

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]