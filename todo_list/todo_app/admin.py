from django.contrib import admin
from .models import TaskModel

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_title', 'task_description', 'is_completed')
    
admin.site.register(TaskModel, TaskModelAdmin)
