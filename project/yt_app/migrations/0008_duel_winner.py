# Generated by Django 4.0.3 on 2022-03-31 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yt_app', '0007_duel_match_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='duel',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='yt_app.team'),
        ),
    ]