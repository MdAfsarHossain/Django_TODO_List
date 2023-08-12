from django.urls import path 
from .views import home, add_task, show_tasks, edit_task, delete_task, completed_tasks

urlpatterns = [
    path('', home, name='homepage'),
    path('add_task/', add_task, name='add_task'),
    path('show_tasks/', show_tasks, name='show_tasks'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('completed_tasks/<int:id>', completed_tasks, name='completed_tasks'),
    path('completed_tasks/', completed_tasks, name='completed_tasks_default'),
]