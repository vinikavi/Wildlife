# Generated by Django 2.2.4 on 2019-09-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20190904_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'online'), ('OFFLINE', 'offline')], max_length=10),
        ),
    ]
