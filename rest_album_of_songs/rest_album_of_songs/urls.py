"""rest_album_of_songs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.urls import path, include
from music.views import (
    AllSongsAPIView,
    AllSingersAPIView,
    AlbumAPIView,
    AlbumSongAPIView,
    SongAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/all-songs/', AllSongsAPIView.as_view()),
    path('api/song/<int:id>/', SongAPIView.as_view()),
    path('api/all-singer/', AllSingersAPIView.as_view()),
    path('api/album/<int:id>/', AlbumAPIView.as_view(), name='album_detail'),
    path(
        'api/album-song/<int:id>/',
        AlbumSongAPIView.as_view(),
        name='album_song',
    ),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
