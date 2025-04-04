from django.urls import path
from . import views
from .views import (
    TaskListCreateAPIView, TaskDetailAPIView, 
    MyTasksAPIView, OverdueTasksAPIView
)

urlpatterns = [
    path('task_list/', TaskListCreateAPIView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('my-tasks/', MyTasksAPIView.as_view(), name='my-tasks'),
    path('overdue-tasks/', OverdueTasksAPIView.as_view(), name='overdue-tasks'),
]
