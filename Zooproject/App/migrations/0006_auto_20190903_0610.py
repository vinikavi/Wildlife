# Generated by Django 2.2.4 on 2019-09-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20190903_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adult',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='child',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='totaltickets',
            field=models.IntegerField(),
        ),
    ]