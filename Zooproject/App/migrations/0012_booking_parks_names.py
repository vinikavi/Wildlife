# Generated by Django 2.2.4 on 2019-09-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20190904_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='parks_names',
            field=models.CharField(choices=[('Queen Elizabeth national park', 'Queen Elizabeth national park'), ('Murchison falls national park', 'Murchison falls national park'), ('Bwindi impenetrable national park', 'Bwindi impenetrable national park'), ('Lake Mburo national Park', 'Lake Mburo national Park'), ('Kidepo Valley National Park', 'Kidepo Valley National Park'), ('Semuliki National Park', 'Semuliki National Park'), ('Mt Elgon National Park', 'Mt Elgon National Park'), ('Mgahinga Gorilla National Park', 'Mgahinga Gorilla National Park')], default=1, max_length=35),
            preserve_default=False,
        ),
    ]
