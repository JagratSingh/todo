from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']