# Generated by Django 5.1.1 on 2024-10-16 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_todo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='slug',
        ),
    ]
