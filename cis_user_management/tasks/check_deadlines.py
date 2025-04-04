from django.core.management.base import BaseCommand
from django.utils import timezone
from tasks.models import Task
from notifications.models import Notification
from user.models import User

class Command(BaseCommand):
    help = 'Check for tasks with missed deadlines and send notifications'

    def handle(self, *args, **options):
        now = timezone.now()
        
        # Finding tasks that have been passed their deadline but are not completed or failed.
        overdue_tasks = Task.objects.filter(
            deadline__lt=now,
            status__in=['PENDING', 'IN_PROGRESS']
        )
        
        managers = User.objects.filter(role='MANAGER')
        
        for task in overdue_tasks:
            # Check if notification already exists for this task
            existing_notification = Notification.objects.filter(
                task=task,
                notification_type='DEADLINE_MISSED'
            ).exists()
            
            if not existing_notification:
                # Create notification for all managers
                for manager in managers:
                    Notification.objects.create(
                        user=manager,
                        task=task,
                        notification_type='DEADLINE_MISSED',
                        message=f"Task '{task.title}' assigned to {task.assigned_to.email} has missed its deadline."
                    )
                
                self.stdout.write(
                    self.style.SUCCESS(f"Created deadline missed notification for task: {task.title}")
                )
