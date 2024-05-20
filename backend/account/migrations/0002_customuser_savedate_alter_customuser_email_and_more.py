# Generated by Django 4.1.13 on 2024-05-20 12:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='savedate',
            field=models.DateTimeField(auto_now=True, verbose_name='Kayıt Tarihi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='facebook_link',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='İsim Soyad'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='instagram_link',
            field=models.URLField(blank=True, null=True, verbose_name='İnstegram URL'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedn URL'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Şifre'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Kullanıcı Adı'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='x_link',
            field=models.URLField(blank=True, null=True, verbose_name='X URL'),
        ),
    ]
