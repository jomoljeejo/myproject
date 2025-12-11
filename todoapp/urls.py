from django.urls import path
from todoapp import controller

urlpatterns = [
    path('todos/', controller.list_todos, name='list_todos'),
    path('todos/create/', controller.create_todo, name='create_todo'),
    path('todos/<int:pk>/', controller.retrieve_todo, name='retrieve_todo'),
    path('todos/<int:pk>/update/', controller.update_todo, name='update_todo'),
    path('todos/<int:pk>/delete/', controller.delete_todo, name='delete_todo'),
]


