from django.urls import path
from . import views

urlpatterns = [
    path("helloWorld/", views.helloWorld, name='helloWorld'),
    path("listaTarefas/", views.listaTarefas, name='listaTarefas')
]