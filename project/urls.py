from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('api/todo/', include('feature.todoapp.urls')),
    path("api/music/", include("feature.musicapp.urls")),
    path("api/artist/", include("feature.artistapp.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
