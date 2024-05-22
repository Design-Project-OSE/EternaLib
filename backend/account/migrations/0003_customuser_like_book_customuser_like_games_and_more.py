# Generated by Django 5.0.6 on 2024-05-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='like_book',
            field=models.IntegerField(default=0, verbose_name='Beğendiği Kitap Sayısı'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='like_games',
            field=models.IntegerField(default=0, verbose_name='Beğendiği Oyun Sayısı'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='like_movie',
            field=models.IntegerField(default=0, verbose_name='Beğendiği Film Sayısı'),
        ),
    ]