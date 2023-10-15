from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def listaTarefas(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskViewSpecific(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task':task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    
    form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form})

def helloWorld(request):
    return HttpResponse('hello World')

def retornaNome(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
