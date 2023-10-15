from django.urls import path
from . import views

urlpatterns = [
    # path("", views.helloWorld, name='helloWorld'),
    path("", views.listaTarefas, name='listaTarefas'),
    path("yourName/<str:name>", views.retornaNome, name='retornaNome'),
]