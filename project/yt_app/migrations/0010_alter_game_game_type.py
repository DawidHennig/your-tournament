# Generated by Django 4.0.3 on 2022-04-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_app', '0009_game_remove_place_tournaments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.IntegerField(choices=[(1, 'RTS'), (2, 'FPS'), (3, 'MOBA'), (4, 'Other')]),
        ),
    ]