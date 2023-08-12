from django.db import models

# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    task_title = models.CharField(max_length = 30)
    task_description = models.TextField()
    is_completed = models.BooleanField(default = False)
    
    class Meta:
        ordering = ['id']
    
    
    