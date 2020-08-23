from django.shortcuts import render, redirect
from .forms import *


def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'tasks/delete.html', context)
