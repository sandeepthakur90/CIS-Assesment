from rest_framework import serializers
from .models import Notification
from tasks.serializers import TaskSerializer

class NotificationSerializer(serializers.ModelSerializer):
    task_details = TaskSerializer(source='task', read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'user', 'task', 'notification_type', 'message', 'is_read', 'created_at', 'task_details']
        read_only_fields = ['id', 'user', 'task', 'notification_type', 'message', 'created_at']
