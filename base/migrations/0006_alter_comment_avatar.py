# Generated by Django 4.1 on 2022-08-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_profile_id_user_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.TextField(default='default.jpg'),
        ),
    ]