# Generated by Django 2.2.4 on 2019-08-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('mobileno', models.CharField(max_length=10)),
            ],
        ),
    ]
