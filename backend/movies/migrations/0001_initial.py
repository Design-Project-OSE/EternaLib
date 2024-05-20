# Generated by Django 4.1.13 on 2024-05-20 11:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Film Kategori ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tür İsmi')),
                ('catshort', models.CharField(max_length=3, verbose_name='Tür Kısaltma')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'verbose_name': 'Film Kategori',
                'verbose_name_plural': 'Film Kategorileri',
            },
        ),
        migrations.CreateModel(
            name='Movies_Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Film Yorum ID')),
                ('userID', models.CharField(max_length=100, verbose_name='Kullanıcı ID')),
                ('movieID', models.CharField(max_length=100, verbose_name='Film ID')),
                ('comment', models.TextField(max_length=2000, verbose_name='Yorum')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'verbose_name': 'Film Yorum',
                'verbose_name_plural': 'Film Yorumları',
            },
        ),
        migrations.CreateModel(
            name='Movies_Like',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Film Beğeni ID')),
                ('userID', models.CharField(max_length=100, verbose_name='Kullanıcı ID')),
                ('movieID', models.CharField(max_length=100, verbose_name='Film ID')),
                ('like', models.BooleanField(verbose_name='beğeni')),
                ('dislike', models.BooleanField(verbose_name='beğenmeme')),
                ('savedate', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
            options={
                'verbose_name': 'Film Beğeni',
                'verbose_name_plural': 'Film Beğenileri',
            },
        ),
        migrations.CreateModel(
            name='Movies_Table',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Film ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('urlname', models.CharField(max_length=100, verbose_name='Url İsmi')),
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
                ('like', models.IntegerField(verbose_name='Beğeniler')),
                ('dislike', models.IntegerField(verbose_name='Beğenilmeyenler')),
                ('commentscount', models.IntegerField(verbose_name='Yorum sayısı')),
                ('categories', models.ManyToManyField(to='movies.movies_category', verbose_name='Kategoriler')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
            },
        ),
    ]
