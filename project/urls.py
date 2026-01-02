from django.urls import path, include

urlpatterns = [
    path('api/todo/', include('feature.todoapp.urls')),
    path("api/music/", include("feature.musicapp.urls")),
    path("api/artist/", include("feature.artistapp.urls")),
]

