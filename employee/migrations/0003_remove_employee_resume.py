# Generated by Django 3.2.8 on 2021-11-01 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_blogger_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='resume',
        ),
    ]
