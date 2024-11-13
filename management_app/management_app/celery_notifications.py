from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_daily_notification():
    inactive_users = User.objects.filter(last_login__lt=timezone.now() - timedelta(days=2))
    for user in inactive_users:
        send_mail(
            'Reminder to log in',
            'You haven’t logged in for more than 2 days. Please log in to stay updated.',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
