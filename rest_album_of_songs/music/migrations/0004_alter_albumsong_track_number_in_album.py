# Generated by Django 4.1 on 2023-08-18 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_albumsong_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumsong',
            name='track_number_in_album',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]