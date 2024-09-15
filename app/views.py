from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskFormSet, NonModelTaskForm

def manage_tasks(request):
    if request.method == 'POST':
        formset = TaskFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Tasks have been successfully updated.")
            return redirect('task_list')
        else:
            messages.error(request, "There was an error updating the tasks.")
    else:
        formset = TaskFormSet(queryset=Task.objects.all())
    
    return render(request, 'manage_tasks.html', {'formset': formset})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = NonModelTaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                completed=form.cleaned_data['completed']
            )
            messages.success(request, "Task has been successfully added.")
            return redirect('task_list')
        else:
            messages.error(request, "There was an error adding the task.")
    else:
        form = NonModelTaskForm()
    
    return render(request, 'add_task.html', {'form': form})
