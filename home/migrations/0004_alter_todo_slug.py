# Generated by Django 5.1.1 on 2024-10-16 07:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_todo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
