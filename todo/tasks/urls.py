from django.urls import path
from . import views

urlpatterns = [
    # path("", views.helloWorld, name='helloWorld'),
    path("", views.listaTarefas, name='listaTarefas'),
    path("task/<int:id>", views.taskView, name='listaTarefa'),
    path("yourName/<str:name>", views.retornaNome, name='retornaNome'),
]