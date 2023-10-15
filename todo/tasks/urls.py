from django.urls import path
from . import views

urlpatterns = [
    # path("", views.helloWorld, name='helloWorld'),
    path("", views.listaTarefas, name='listaTarefas'),
    path("task/<int:id>", views.taskViewSpecific, name='listaTarefaEspecífica'),
    path("newtask/", views.newTask, name="newTask"),
    path("edittask/<int:id>", views.editTask, name="editTask"),
    path("yourName/<str:name>", views.retornaNome, name='retornaNome'),
]