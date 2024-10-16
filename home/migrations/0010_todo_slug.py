# Generated by Django 5.1.1 on 2024-10-16 07:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_todo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title', unique=True),
        ),
    ]
