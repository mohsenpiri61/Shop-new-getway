# Generated by Django 4.2.16 on 2024-11-29 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_paymentnumber_paymentmodel_ref_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmodel',
            old_name='ref_id',
            new_name='payment_number',
        ),
        migrations.RemoveField(
            model_name='paymentmodel',
            name='authority_id',
        ),
        migrations.RemoveField(
            model_name='paymentmodel',
            name='response_code',
        ),
    ]