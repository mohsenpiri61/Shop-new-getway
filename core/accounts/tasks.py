from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reset_password_email(subject, message, from_email, recipient_list):
    # ارسال ایمیل بازیابی رمز عبور
    send_mail(subject, message, from_email, recipient_list)
