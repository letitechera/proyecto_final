# Generated by Django 4.2.1 on 2023-06-13 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='app_user_id',
            new_name='app_user',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='app_user_id',
            new_name='app_user',
        ),
    ]
