# Generated by Django 4.1 on 2023-08-18 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_albumsong_track_number_in_album'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='albumsong',
            unique_together={('track_number_in_album', 'album')},
        ),
    ]
