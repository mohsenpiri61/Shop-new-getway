from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reset_password_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'webmasterl@localhost',
        recipient_list,
        fail_silently=False,
    )