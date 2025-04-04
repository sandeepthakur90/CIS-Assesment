from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tasks.models import Task
from django.utils import timezone
from .utils import send_overdue_task_email
from user.permissions import IsAdmin

class NotifyManagersAboutOverdueTasksAPIView(APIView):
    """
    Send email to managers if a user's task is overdue and not completed or failed.
    """
    permission_classes = [IsAdmin]  # Only Admin should trigger this

    def post(self, request, format=None):
        now = timezone.now()
        overdue_tasks = Task.objects.filter(
            deadline__lt=now,
            status__in=['PENDING', 'IN_PROGRESS']
        )

        notified = []

        for task in overdue_tasks:
            assigned_user = task.assigned_to
            manager = task.assigned_by

            if manager.role == 'MANAGER':
                send_overdue_task_email(
                    to_email=manager.email,
                    task_title=task.title,
                    user_email=assigned_user.email
                )
                notified.append({
                    "manager": manager.email,
                    "task": task.title,
                    "assigned_user": assigned_user.email
                })

        return Response({
            "message": "Emails sent to managers for overdue tasks.",
            "notified": notified
        }, status=status.HTTP_200_OK)
