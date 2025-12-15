from django.urls import path
from project.feature.todoapp import controller

urlpatterns = [
    path('create/', controller.create_todo, name='create_todo'),
    path('get_all/', controller.list_todos, name='list_todos'),
    path('get/', controller.retrieve_todo, name='retrieve_todo'),
    path('update/', controller.update_todo, name='update_todo'),
    path('delete/', controller.delete_todo, name='delete_todo'),
]



