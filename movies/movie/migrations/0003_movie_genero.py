# Generated by Django 4.2.6 on 2023-10-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genero',
            field=models.CharField(default='accion', max_length=50),
            preserve_default=False,
        ),
    ]
