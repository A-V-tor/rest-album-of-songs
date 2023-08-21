from django.contrib import admin
from .models import Song, Singer, Album, AlbumSong


admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(AlbumSong)
