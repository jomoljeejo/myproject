
from django.urls import path
from feature.todoapp.controller import TodoController

urlpatterns = [
    path('create/', TodoController.create, name='create_todo'),
    path('get_all/', TodoController.get_all, name='list_todos'),
    path('get/', TodoController.get_one, name='retrieve_todo'),
    path('update/', TodoController.update, name='update_todo'),
    path('delete/', TodoController.delete, name='delete_todo'),
]



