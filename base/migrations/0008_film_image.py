# Generated by Django 4.1 on 2022-08-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_film_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
