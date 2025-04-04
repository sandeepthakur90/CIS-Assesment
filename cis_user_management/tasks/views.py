from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from user.permissions import IsAdmin, IsAdminOrManager
from user.models import User
from notifications.models import Notification


class TaskListCreateAPIView(APIView):
    """
    List all tasks or create a new task
    """
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrManager()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        
        # Admin can see all tasks
        if user.role == 'ADMIN':
            return Task.objects.all()
        
        # Manager can see tasks they created or all tasks assigned to their users
        elif user.role == 'MANAGER':
            return Task.objects.filter(Q(assigned_by=user) | Q(assigned_to__role='USER'))
        
        # Regular users can only see their own tasks
        else:
            return Task.objects.filter(assigned_to=user)
    
    def get(self, request, format=None):
        tasks = self.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # Set the current user as the one who assigned the task
            task = serializer.save(assigned_by=request.user)
            
            # Create notification for the assigned user
            Notification.objects.create(
                user=task.assigned_to,
                task=task,
                notification_type='TASK_ASSIGNED',
                message=f"You have been assigned a new task: {task.title}"
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    """
    Retrieve, update or delete a task instance
    """
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminOrManager()]
        return [IsAuthenticated()]
    
    def get_object(self, pk):
        user = self.request.user
        task = get_object_or_404(Task, pk=pk)
        
        # Check if user has permission to access this task
        if user.role == 'ADMIN':
            return task
        elif user.role == 'MANAGER':
            if task.assigned_by == user or task.assigned_to.role == 'USER':
                return task
        elif task.assigned_to == user:
            return task
            
        # If we get here, user doesn't have permission
        self.permission_denied(self.request)
        
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        old_status = task.status
        
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            new_status = task.status
            
            # If task status changed to FAILED
            if old_status != 'FAILED' and new_status == 'FAILED':
                user = task.assigned_to
                user.failed_tasks_count += 1
                
                # Check if user has failed 5 or more tasks
                if user.failed_tasks_count >= 5:
                    user.is_active = False
                    
                    # Notify managers about user deactivation
                    managers = User.objects.filter(role='MANAGER')
                    for manager in managers:
                        Notification.objects.create(
                            user=manager,
                            task=task,
                            notification_type='USER_DEACTIVATED',
                            message=f"User {user.email} has been deactivated due to failing 5 or more tasks."
                        )
                
                user.save()
            
            # If deadline is missed
            if task.deadline < timezone.now() and task.status not in ['COMPLETED', 'FAILED']:
                # Notify managers about missed deadline
                managers = User.objects.filter(role='MANAGER')
                for manager in managers:
                    Notification.objects.create(
                        user=manager,
                        task=task,
                        notification_type='DEADLINE_MISSED',
                        message=f"Task '{task.title}' assigned to {task.assigned_to.email} has missed its deadline."
                    )
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        task = self.get_object(pk)
        old_status = task.status
        
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            task = serializer.save()
            new_status = task.status
            
            # If task status changed to FAILED
            if old_status != 'FAILED' and new_status == 'FAILED':
                user = task.assigned_to
                user.failed_tasks_count += 1
                
                # Check if user has failed 5 or more tasks
                if user.failed_tasks_count >= 5:
                    user.is_active = False
                    
                    # Notify managers about user deactivation
                    managers = User.objects.filter(role='MANAGER')
                    for manager in managers:
                        Notification.objects.create(
                            user=manager,
                            task=task,
                            notification_type='USER_DEACTIVATED',
                            message=f"User {user.email} has been deactivated due to failing 5 or more tasks."
                        )
                
                user.save()
            
            # If deadline is missed
            if task.deadline < timezone.now() and task.status not in ['COMPLETED', 'FAILED']:
                # Notify managers about missed deadline
                managers = User.objects.filter(role='MANAGER')
                for manager in managers:
                    Notification.objects.create(
                        user=manager,
                        task=task,
                        notification_type='DEADLINE_MISSED',
                        message=f"Task '{task.title}' assigned to {task.assigned_to.email} has missed its deadline."
                    )
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyTasksAPIView(APIView):
    """
    List all tasks assigned to the current user
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        tasks = Task.objects.filter(assigned_to=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class OverdueTasksAPIView(APIView):
    """
    List all overdue tasks
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        now = timezone.now()
        tasks = Task.objects.filter(deadline__lt=now, status__in=['PENDING', 'IN_PROGRESS'])
        
        if request.user.role == 'USER':
            tasks = tasks.filter(assigned_to=request.user)
        elif request.user.role == 'MANAGER':
            tasks = tasks.filter(Q(assigned_by=request.user) | Q(assigned_to__role='USER'))
        
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
