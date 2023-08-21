from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Singer(models.Model):
    name = models.CharField(
        max_length=255, verbose_name='Имя/Название', unique=True
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.IntegerField(null=False)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    track_number_in_album = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.album}: {self.song}'

    @receiver(pre_save, sender='music.AlbumSong')
    def set_track_number(sender, instance, **kwargs):
        if not instance.track_number_in_album:
            # максимальный номер трека для данного альбома
            max_track_number = AlbumSong.objects.filter(
                album=instance.album
            ).aggregate(models.Max('track_number_in_album'))[
                'track_number_in_album__max'
            ]
            # следующий номер трека
            instance.track_number_in_album = (max_track_number or 0) + 1

    class Meta:
        unique_together = ('track_number_in_album', 'album')
