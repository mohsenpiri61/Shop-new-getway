# Generated by Django 4.2.16 on 2024-11-12 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_failedloginattempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failedloginattempt',
            name='username',
        ),
        migrations.AddField(
            model_name='failedloginattempt',
            name='email',
            field=models.EmailField(default='admin@mysite.com', max_length=254),
        ),
    ]
