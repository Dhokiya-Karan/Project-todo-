from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tasks
from .forms import *


# Create your views here.
def index(request):
    task = tasks.objects.all()
    form = Taskform()
    
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'task':task,'form':form}
    return render(request, 'tasks/list.html', context)

def update_task(request, pk):
    task = tasks.objects.get(id=pk)
    form = Taskform(instance=task)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    item = tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html',context)