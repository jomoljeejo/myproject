# todoapp/urls.py
from django.urls import path
from todoapp import controller

urlpatterns = [
    path('todo/create/', controller.todo_create, name='todo-create'),
    path('todo/<int:pk>/', controller.todo_retrieve, name='todo-get'),
    path('todo/<int:pk>/update/', controller.todo_update, name='todo-update'),
    path('todo/<int:pk>/partial-update/', controller.todo_partial_update, name='todo-partial-update'),
    path('todo/delete-many/', controller.todo_delete_many, name='todo-delete-many'),
    path('todo/', controller.todo_list, name='todo-list'),
]
