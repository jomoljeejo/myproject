from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo-list'),
    path('todos/create/', views.todo_create, name='todo-create'),
    path('todos/<int:pk>/', views.todo_retrieve, name='todo-retrieve'),
    path('todos/<int:pk>/update/', views.todo_update, name='todo-update'),
    path('todos/<int:pk>/partial/', views.todo_partial_update, name='todo-partial'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo-delete'),
]
