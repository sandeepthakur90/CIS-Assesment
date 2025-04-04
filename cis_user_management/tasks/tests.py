from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch

from tasks.models import Task
from user.models import User
from notifications.models import Notification


class TaskListCreateAPIViewTest(TestCase):
    def setUp(self):
        # Create users with different roles
        self.admin_user = User.objects.create_user(
            email='admin@example.com',
            password='password123',
            role='ADMIN'
        )
        
        self.manager_user = User.objects.create_user(
            email='manager@example.com',
            password='password123',
            role='MANAGER'
        )
        
        self.regular_user = User.objects.create_user(
            email='user@example.com',
            password='password123',
            role='USER'
        )
        
        # Create some tasks
        self.admin_task = Task.objects.create(
            title='Admin Task',
            description='Task created by admin',
            deadline=timezone.now() + timedelta(days=7),
            status='PENDING',
            assigned_to=self.regular_user,
            assigned_by=self.admin_user
        )
        
        self.manager_task = Task.objects.create(
            title='Manager Task',
            description='Task created by manager',
            deadline=timezone.now() + timedelta(days=7),
            status='PENDING',
            assigned_to=self.regular_user,
            assigned_by=self.manager_user
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('task-list-create')
    
    def test_get_tasks_as_admin(self):
        """Test that admin can see all tasks"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Admin should see all tasks
    
    def test_get_tasks_as_manager(self):
        """Test that manager can see tasks they created or assigned to users"""
        self.client.force_authenticate(user=self.manager_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Manager should see tasks they created or assigned to users
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Manager Task')
    
    def test_get_tasks_as_user(self):
        """Test that regular user can only see their own tasks"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # User should see tasks assigned to them
    
    def test_create_task_as_admin(self):
        """Test that admin can create a task"""
        self.client.force_authenticate(user=self.admin_user)
        
        task_data = {
            'title': 'New Admin Task',
            'description': 'Task created in test',
            'deadline': (timezone.now() + timedelta(days=5)).isoformat(),
            'status': 'PENDING',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.post(self.url, task_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Notification.objects.count(), 1)  # Notification should be created
    
    def test_create_task_as_manager(self):
        """Test that manager can create a task"""
        self.client.force_authenticate(user=self.manager_user)
        
        task_data = {
            'title': 'New Manager Task',
            'description': 'Task created in test',
            'deadline': (timezone.now() + timedelta(days=5)).isoformat(),
            'status': 'PENDING',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.post(self.url, task_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Notification.objects.count(), 1)  # Notification should be created
    
    def test_create_task_as_user(self):
        """Test that regular user cannot create a task"""
        self.client.force_authenticate(user=self.regular_user)
        
        task_data = {
            'title': 'New User Task',
            'description': 'Task created in test',
            'deadline': (timezone.now() + timedelta(days=5)).isoformat(),
            'status': 'PENDING',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.post(self.url, task_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Task.objects.count(), 2)  # No new task should be created


class TaskDetailAPIViewTest(TestCase):
    def setUp(self):
        # Create users with different roles
        self.admin_user = User.objects.create_user(
            email='admin@example.com',
            password='password123',
            role='ADMIN'
        )
        
        self.manager_user = User.objects.create_user(
            email='manager@example.com',
            password='password123',
            role='MANAGER'
        )
        
        self.regular_user = User.objects.create_user(
            email='user@example.com',
            password='password123',
            role='USER'
        )
        
        self.other_user = User.objects.create_user(
            email='other@example.com',
            password='password123',
            role='USER'
        )
        
        # Create a task
        self.task = Task.objects.create(
            title='Test Task',
            description='Task for testing',
            deadline=timezone.now() + timedelta(days=7),
            status='PENDING',
            assigned_to=self.regular_user,
            assigned_by=self.manager_user
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('task-detail', args=[self.task.id])
    
    def test_get_task_as_admin(self):
        """Test that admin can view any task"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')
    
    def test_get_task_as_manager(self):
        """Test that manager can view task they created"""
        self.client.force_authenticate(user=self.manager_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')
    
    def test_get_task_as_assigned_user(self):
        """Test that assigned user can view their task"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')
    
    def test_get_task_as_other_user(self):
        """Test that other users cannot view tasks not assigned to them"""
        self.client.force_authenticate(user=self.other_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_update_task_as_admin(self):
        """Test that admin can update any task"""
        self.client.force_authenticate(user=self.admin_user)
        
        updated_data = {
            'title': 'Updated Task',
            'description': 'Updated description',
            'deadline': (timezone.now() + timedelta(days=10)).isoformat(),
            'status': 'IN_PROGRESS',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.put(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.status, 'IN_PROGRESS')
    
    def test_update_task_as_manager(self):
        """Test that manager can update task they created"""
        self.client.force_authenticate(user=self.manager_user)
        
        updated_data = {
            'title': 'Manager Updated Task',
            'description': 'Updated by manager',
            'deadline': (timezone.now() + timedelta(days=10)).isoformat(),
            'status': 'IN_PROGRESS',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.put(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Manager Updated Task')
    
    def test_update_task_as_user(self):
        """Test that regular user cannot update task"""
        self.client.force_authenticate(user=self.regular_user)
        
        updated_data = {
            'title': 'User Updated Task',
            'description': 'Updated by user',
            'deadline': (timezone.now() + timedelta(days=10)).isoformat(),
            'status': 'IN_PROGRESS',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.put(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Test Task')  # Title should not change
    
    def test_mark_task_as_failed(self):
        """Test that marking a task as failed updates user's failed_tasks_count"""
        self.client.force_authenticate(user=self.admin_user)
        
        updated_data = {
            'title': 'Failed Task',
            'description': 'This task failed',
            'deadline': (timezone.now() + timedelta(days=10)).isoformat(),
            'status': 'FAILED',
            'assigned_to': self.regular_user.id
        }
        
        response = self.client.patch(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertEqual(self.regular_user.failed_tasks_count, 1)
    
    def test_deactivate_user_after_five_failures(self):
        """Test that user is deactivated after failing 5 tasks"""
        self.regular_user.failed_tasks_count = 4
        self.regular_user.save()
        
        self.client.force_authenticate(user=self.admin_user)
        
        updated_data = {
            'status': 'FAILED',
        }
        
        response = self.client.patch(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertEqual(self.regular_user.failed_tasks_count, 5)
        self.assertFalse(self.regular_user.is_active)
        
        # Check that notifications were created for managers
        notifications = Notification.objects.filter(notification_type='USER_DEACTIVATED')
        self.assertEqual(notifications.count(), 1)
    
    def test_delete_task_as_admin(self):
        """Test that admin can delete a task"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
    
    def test_delete_task_as_user(self):
        """Test that regular user cannot delete a task"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Task.objects.count(), 1)


class MyTasksAPIViewTest(TestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(
            email='user1@example.com',
            password='password123',
            role='USER'
        )
        
        self.user2 = User.objects.create_user(
            email='user2@example.com',
            password='password123',
            role='USER'
        )
        
        self.manager = User.objects.create_user(
            email='manager@example.com',
            password='password123',
            role='MANAGER'
        )
        
        # Create tasks for user1
        self.task1 = Task.objects.create(
            title='User1 Task 1',
            description='First task for user1',
            deadline=timezone.now() + timedelta(days=7),
            status='PENDING',
            assigned_to=self.user1,
            assigned_by=self.manager
        )
        
        self.task2 = Task.objects.create(
            title='User1 Task 2',
            description='Second task for user1',
            deadline=timezone.now() + timedelta(days=10),
            status='IN_PROGRESS',
            assigned_to=self.user1,
            assigned_by=self.manager
        )
        
        # Create task for user2
        self.task3 = Task.objects.create(
            title='User2 Task',
            description='Task for user2',
            deadline=timezone.now() + timedelta(days=5),
            status='PENDING',
            assigned_to=self.user2,
            assigned_by=self.manager
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('my-tasks')
    
    def test_get_my_tasks(self):
        """Test that user can see only their tasks"""
        self.client.force_authenticate(user=self.user1)
        response = self.client.get
        self.assertEqual(response.status_code, status.HTTP_200_OK)