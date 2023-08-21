from .models import Song, Singer, Album, AlbumSong
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    singer = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = '__all__'

    def get_singer(self, obj):
        singer = obj.singer
        return {
            'id': singer.id,
            'name': singer.name,
        }


class AlbumSongSerializer(serializers.ModelSerializer):
    song = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()
    singer = serializers.SerializerMethodField()

    class Meta:
        model = AlbumSong
        fields = '__all__'

    def get_song(self, obj):
        song = obj.song
        return {
            'id': song.id,
            'name': song.name,
        }

    def get_album(self, obj):
        album = obj.album
        return {
            'id': album.id,
            'name': album.name,
            'year': album.year,
        }

    def get_singer(self, obj):
        singer = obj.album.singer
        return {
            'id': singer.id,
            'name': singer.name,
        }


class SongSerializer(serializers.ModelSerializer):
    # source указывает на обратное отношение к AlbumSong
    albums = AlbumSongSerializer(
        source='albumsong_set', many=True, read_only=True
    )

    class Meta:
        model = Song
        fields = '__all__'
