# Generated by Django 5.1.1 on 2024-10-16 07:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_todo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=True, editable=False, populate_from='title', unique=True),
        ),
    ]
