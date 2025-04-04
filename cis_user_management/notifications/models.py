from django.db import models
from django.conf import settings
from tasks.models import Task

class Notification(models.Model):
    TYPE_CHOICES = (
        ('DEADLINE_MISSED', 'Deadline Missed'),
        ('USER_DEACTIVATED', 'User Deactivated'),
        ('TASK_ASSIGNED', 'Task Assigned'),
        ('TASK_UPDATED', 'Task Updated'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.notification_type} - {self.user.email}"
