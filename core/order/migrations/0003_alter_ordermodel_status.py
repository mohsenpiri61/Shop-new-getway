# Generated by Django 4.2.16 on 2024-11-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_ordermodel_city_remove_ordermodel_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'در انتظار پرداخت'), (2, 'پرداخت شده'), (3, 'لغو شده')], default=1),
        ),
    ]