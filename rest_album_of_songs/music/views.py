from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song, Singer, Album, AlbumSong
from .serializers import (
    SongSerializer,
    SingerSerializer,
    AlbumSerializer,
    AlbumSongSerializer,
)


class AllSongsAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongAPIView(generics.ListAPIView):
    def get_object(self, id):
        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        return Response(serializer.data)


class AllSingersAPIView(generics.ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class AlbumAPIView(APIView):
    def get_object(self, id):
        try:
            return Album.objects.get(id=id)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, id):
        sing = self.get_object(id)
        serializer = AlbumSerializer(sing)
        return Response(serializer.data)


class AlbumSongAPIView(APIView):
    def get_object(self, id):
        try:
            return AlbumSong.objects.get(id=id)
        except AlbumSong.DoesNotExist:
            raise Http404

    def get(self, request, id):
        sing = self.get_object(id)
        serializer = AlbumSongSerializer(sing)
        return Response(serializer.data)
