from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.

# Home Page
def home(request):
    return render(request, 'home.html')


# Add Todo List
def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_tasks')
    else:
        task = TaskForm()
    return render(request, 'add_task.html', {'task': task})


# Show Todo List
def show_tasks(request):
    task = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'task': task})


# Edit Todo List
def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance = task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'edit_task.html', {'task': form})


# Delete Todo List
def delete_task(request, id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect('show_tasks')


# Complete Todo List
def completed_tasks(request, id=None):
    if id is None:
        tasks = TaskModel.objects.all()
        return render(request, 'completed_tasks.html', {'task': tasks})
    else:
        tasks = TaskModel.objects.get(pk=id)
        tasks.is_completed = True
        tasks.save()
        return redirect('completed_tasks_default')
      
      
      