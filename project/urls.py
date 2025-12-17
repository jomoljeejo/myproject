from django.urls import path, include

urlpatterns = [
    path('api/todo/', include('project.feature.todoapp.urls')),
    path("api/music/", include("project.feature.musicapp.urls")),
]

