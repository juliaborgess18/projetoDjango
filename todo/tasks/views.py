from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloWorld(request):
    return HttpResponse('hello World')

def listaTarefas(request):
    return render(request, 'tasks/list.html')
