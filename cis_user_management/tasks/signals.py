from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from notifications.models import Notification

@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.assigned_to,
            task=instance,
            notification_type='TASK_ASSIGNED',
            message=f"You have been assigned a new task: {instance.title}"
        )
    else:
        if instance.status == 'FAILED':
            user = instance.assigned_to
            
            if user.failed_tasks_count >= 5 and user.is_active:
                user.is_active = False
                user.save()
                
                # Notify managers about user deactivation
                managers = User.objects.filter(role='MANAGER')
