# Generated by Django 4.1.13 on 2024-05-20 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Oyun Kategori ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tür İsmi')),
                ('catshort', models.CharField(max_length=3, verbose_name='Tür Kısaltma')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'verbose_name': 'Oyun Kategori',
                'verbose_name_plural': 'Oyun Kategorileri',
            },
        ),
        migrations.CreateModel(
            name='Game_Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Oyun Yorum ID')),
                ('userID', models.CharField(max_length=100, verbose_name='Kullanıcı ID')),
                ('gameID', models.CharField(max_length=100, verbose_name='Oyun ID')),
                ('comment', models.TextField(max_length=2000, verbose_name='Yorum')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'verbose_name': 'Oyun Yorum',
                'verbose_name_plural': 'Oyun Yorum',
            },
        ),
        migrations.CreateModel(
            name='Game_Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Oyun Beğeni ID')),
                ('userID', models.CharField(max_length=100, verbose_name='Kullanıcı ID')),
                ('gameID', models.CharField(max_length=100, verbose_name='Oyun ID')),
                ('like', models.BooleanField(verbose_name='beğeni')),
                ('dislike', models.BooleanField(verbose_name='beğenmeme')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'verbose_name': 'Oyun Beğeni',
                'verbose_name_plural': 'Oyun Beğenileri',
            },
        ),
        migrations.CreateModel(
            name='Games_Table',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Oyun ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('urlname', models.CharField(max_length=100, verbose_name='URL İsmi')),
                ('production', models.CharField(max_length=100, verbose_name='Yapımcı')),
                ('about', models.TextField(max_length=2000, verbose_name='Hakkında')),
                ('release', models.DateTimeField(verbose_name='Çıkış Tarihi')),
                ('imdb', models.FloatField(verbose_name='IMDB')),
                ('metacritic', models.FloatField(verbose_name='Metacritic')),
                ('background', models.URLField(verbose_name='Arkaplan URL')),
                ('poster', models.URLField(verbose_name='Poster URL')),
                ('trailer', models.URLField(verbose_name='Trailer URL')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
                ('isPublished', models.BooleanField(default=True, verbose_name='Yayın Durumu')),
                ('like', models.IntegerField(default=0, verbose_name='Beğeni sayısı')),
                ('dislike', models.IntegerField(default=0, verbose_name='Beğenilmeyen')),
                ('categories', models.ManyToManyField(to='game.game_category', verbose_name='Tür')),
            ],
            options={
                'verbose_name': 'Oyun',
                'verbose_name_plural': 'Oyunlar',
            },
        ),
    ]
