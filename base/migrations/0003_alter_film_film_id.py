# Generated by Django 4.1 on 2022-08-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_film_created_film_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_id',
            field=models.BigIntegerField(),
        ),
    ]
