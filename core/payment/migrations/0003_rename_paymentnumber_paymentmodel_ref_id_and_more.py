# Generated by Django 4.2.16 on 2024-11-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_ref_id_paymentmodel_paymentnumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentmodel',
            old_name='paymentnumber',
            new_name='ref_id',
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='authority_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paymentmodel',
            name='response_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
