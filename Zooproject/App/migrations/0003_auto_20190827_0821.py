# Generated by Django 2.2.4 on 2019-08-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
