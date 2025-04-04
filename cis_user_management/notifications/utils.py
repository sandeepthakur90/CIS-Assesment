from django.core.mail import send_mail
from django.conf import settings

def send_overdue_task_email(to_email, task_title, user_email):
    subject = "Overdue Task Alert"
    message = f"""
    Hello Manager,

    The task titled '{task_title}' assigned to user {user_email} is overdue and not yet completed or marked as failed.

    Please take the necessary actions.

    Regards,
    Task Management System
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )
