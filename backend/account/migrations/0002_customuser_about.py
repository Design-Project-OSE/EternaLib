# Generated by Django 5.0.6 on 2024-05-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Hakkında'),
        ),
    ]
