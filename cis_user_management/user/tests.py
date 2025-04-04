from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListCreateAPIViewTest(TestCase):
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
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('user-list-create')
    
    def test_list_users_as_admin(self):
        """Test that admin can list all users"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Should see all users
    
    def test_list_users_as_manager(self):
        """Test that manager can list all users"""
        self.client.force_authenticate(user=self.manager_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Should see all users
    
    def test_list_users_as_regular_user(self):
        """Test that regular user can list all users"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Should see all users
    
    def test_create_user_as_admin(self):
        """Test that admin can create a new user"""
        self.client.force_authenticate(user=self.admin_user)
        
        user_data = {
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'role': 'USER',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = self.client.post(self.url, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 4)
        self.assertEqual(User.objects.get(email='newuser@example.com').role, 'USER')
    
    def test_create_user_as_manager(self):
        """Test that manager cannot create a new user"""
        self.client.force_authenticate(user=self.manager_user)
        
        user_data = {
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'role': 'USER',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = self.client.post(self.url, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 3)  # No new user should be created
    
    def test_create_user_as_regular_user(self):
        """Test that regular user cannot create a new user"""
        self.client.force_authenticate(user=self.regular_user)
        
        user_data = {
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'role': 'USER',
            'first_name': 'New',
            'last_name': 'User'
        }
        
        response = self.client.post(self.url, user_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 3)  # No new user should be created


class UserDetailAPIViewTest(TestCase):
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
            role='USER',
            first_name='Regular',
            last_name='User'
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('user-detail', args=[self.regular_user.id])
    
    def test_get_user_as_admin(self):
        """Test that admin can view any user"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'user@example.com')
    
    def test_get_user_as_manager(self):
        """Test that manager can view any user"""
        self.client.force_authenticate(user=self.manager_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'user@example.com')
    
    def test_get_user_as_self(self):
        """Test that user can view their own details"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'user@example.com')
    
    def test_update_user_as_admin(self):
        """Test that admin can update any user"""
        self.client.force_authenticate(user=self.admin_user)
        
        updated_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'role': 'USER'
        }
        
        response = self.client.patch(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertEqual(self.regular_user.first_name, 'Updated')
        self.assertEqual(self.regular_user.last_name, 'Name')
    
    def test_update_user_as_self(self):
        """Test that user can update their own details"""
        self.client.force_authenticate(user=self.regular_user)
        
        updated_data = {
            'first_name': 'Self',
            'last_name': 'Updated'
        }
        
        response = self.client.patch(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertEqual(self.regular_user.first_name, 'Self')
        self.assertEqual(self.regular_user.last_name, 'Updated')
    
    def test_update_user_as_other_user(self):
        """Test that user cannot update another user's details"""
        other_user = User.objects.create_user(
            email='other@example.com',
            password='password123',
            role='USER'
        )
        
        self.client.force_authenticate(user=other_user)
        
        updated_data = {
            'first_name': 'Hacked',
            'last_name': 'Name'
        }
        
        response = self.client.patch(self.url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.regular_user.refresh_from_db()
        self.assertEqual(self.regular_user.first_name, 'Regular')  # Name should not change
    
    def test_delete_user_as_admin(self):
        """Test that admin can delete any user"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(email='user@example.com').count(), 0)
    
    def test_delete_user_as_self(self):
        """Test that user can delete their own account"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(email='user@example.com').count(), 0)
    
    def test_delete_user_as_other_user(self):
        """Test that user cannot delete another user's account"""
        other_user = User.objects.create_user(
            email='other@example.com',
            password='password123',
            role='USER'
        )
        
        self.client.force_authenticate(user=other_user)
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.filter(email='user@example.com').count(), 1)


class ReactivateUserAPIViewTest(TestCase):
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
            role='USER',
            is_active=False,
            failed_tasks_count=5
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('reactivate-user', args=[self.regular_user.id])
    
    def test_reactivate_user_as_admin(self):
        """Test that admin can reactivate a deactivated user"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertTrue(self.regular_user.is_active)
        self.assertEqual(self.regular_user.failed_tasks_count, 0)
    
    def test_reactivate_user_as_manager(self):
        """Test that manager can reactivate a deactivated user"""
        self.client.force_authenticate(user=self.manager_user)
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertTrue(self.regular_user.is_active)
        self.assertEqual(self.regular_user.failed_tasks_count, 0)
    
    def test_reactivate_user_as_regular_user(self):
        """Test that regular user cannot reactivate a deactivated user"""
        other_user = User.objects.create_user(
            email='other@example.com',
            password='password123',
            role='USER'
        )
        
        self.client.force_authenticate(user=other_user)
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.regular_user.refresh_from_db()
        self.assertFalse(self.regular_user.is_active)
    
    def test_reactivate_already_active_user(self):
        """Test reactivating an already active user"""
        self.regular_user.is_active = True
        self.regular_user.save()
        
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeactivateUserAPIViewTest(TestCase):
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
            role='USER',
            is_active=True
        )
        
        # Setup API client
        self.client = APIClient()
        self.url = reverse('deactivate-user', args=[self.regular_user.id])
    
    def test_deactivate_user_as_admin(self):
        """Test that admin can deactivate an active user"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertFalse(self.regular_user.is_active)
    
    def test_deactivate_user_as_manager(self):
        """Test that manager can deactivate an active user"""
        self.client.force_authenticate(user=self.manager_user)
        response = self.client.post(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertFalse(self.regular_user.is_active)
    
    def test_deactivate_user_as_regular_user(self):
        """Test that regular user cannot deactivate an active user"""
        other_user = User.objects.create_user(
            email='other@example.com',
            password='password123',
            role='USER'
        )

        self.client.force_authenticate(user=other_user)
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.regular_user.refresh_from_db()
        self.assertTrue(self.regular_user.is_active)

