# Generated by Django 4.1 on 2023-08-18 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='albumsong',
            unique_together={('track_number_in_album', 'song')},
        ),
    ]