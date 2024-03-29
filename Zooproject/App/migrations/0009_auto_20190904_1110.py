# Generated by Django 2.2.4 on 2019-09-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_booking_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='cost',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='idno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
