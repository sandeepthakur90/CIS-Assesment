from rest_framework import serializers
from .models import Task
from user.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_details = UserSerializer(source='assigned_to', read_only=True)
    assigned_by_details = UserSerializer(source='assigned_by', read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'assigned_by', 
                  'status', 'deadline', 'created_at', 'updated_at', 
                  'assigned_to_details', 'assigned_by_details']
        read_only_fields = ['id', 'created_at', 'updated_at', 'assigned_by']
