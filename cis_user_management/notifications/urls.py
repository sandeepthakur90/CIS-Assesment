from django.urls import path
from . import views
from .views import NotifyManagersAboutOverdueTasksAPIView

urlpatterns = [
    path('tasks/notify-managers/', NotifyManagersAboutOverdueTasksAPIView.as_view(), name='notify-managers'),

]
