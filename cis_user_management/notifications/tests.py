from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch

from tasks.models import Task
from user.models import User


class NotifyManagersAboutOverdueTasksAPIViewTest(TestCase):
    def setUp(self):
        # Create admin user for authentication
        self.admin_user = User.objects.create_user(
            email='admin@example.com',
            password='password123',
            role='ADMIN'
        )
        
        # Create a manager
        self.manager = User.objects.create_user(
            email='manager@example.com',
            password='password123',
            role='MANAGER'
        )
        
        # Create a regular user
        self.regular_user = User.objects.create_user(
            email='user@example.com',
            password='password123',
            role='USER'
        )
        
        # Create an overdue task
        self.overdue_task = Task.objects.create(
            title='Overdue Task',
            description='This task is overdue',
            deadline=timezone.now() - timedelta(days=1),
            status='PENDING',
            assigned_to=self.regular_user,
            assigned_by=self.manager
        )
        
        # Create a non-overdue task
        self.active_task = Task.objects.create(
            title='Active Task',
            description='This task is not overdue',
            deadline=timezone.now() + timedelta(days=1),
            status='PENDING',
            assigned_to=self.regular_user,
            assigned_by=self.manager
        )
        
        # Create a completed task that is overdue
        self.completed_task = Task.objects.create(
            title='Completed Task',
            description='This task is overdue but completed',
            deadline=timezone.now() - timedelta(days=1),
            status='COMPLETED',
            assigned_to=self.regular_user,
            assigned_by=self.manager
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('notify-overdue-tasks')
    
    @patch('notifications.views.send_overdue_task_email')
    def test_notify_managers_as_admin(self, mock_send_email):
        """Test that admin can trigger notifications for overdue tasks"""
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Make the request
        response = self.client.post(self.url)
        
        # Check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['notified']), 1)
        self.assertEqual(response.data['notified'][0]['task'], self.overdue_task.title)
        
        # Verify email was sent
        mock_send_email.assert_called_once_with(
            to_email=self.manager.email,
            task_title=self.overdue_task.title,
            user_email=self.regular_user.email
        )
    
    @patch('notifications.views.send_overdue_task_email')
    def test_notify_managers_unauthorized(self, mock_send_email):
        """Test that non-admin users cannot trigger notifications"""
        # Authenticate as regular user
        self.client.force_authenticate(user=self.regular_user)
        
        # Make the request
        response = self.client.post(self.url)
        
        # Check response
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Verify no email was sent
        mock_send_email.assert_not_called()
    
    @patch('notifications.views.send_overdue_task_email')
    def test_notify_managers_no_overdue_tasks(self, mock_send_email):
        """Test behavior when there are no overdue tasks"""
        # Change the status of the overdue task
        self.overdue_task.status = 'COMPLETED'
        self.overdue_task.save()
        
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Make the request
        response = self.client.post(self.url)
        
        # Check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['notified']), 0)
        
        # Verify no email was sent
        mock_send_email.assert_not_called()
    
    @patch('notifications.views.send_overdue_task_email')
    def test_notify_managers_non_manager_assigned_by(self, mock_send_email):
        """Test behavior when task is assigned by non-manager"""
        # Change the role of the manager
        self.manager.role = 'USER'
        self.manager.save()
        
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Make the request
        response = self.client.post(self.url)
        
        # Check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['notified']), 0)
        
        # Verify no email was sent
        mock_send_email.assert_not_called()
