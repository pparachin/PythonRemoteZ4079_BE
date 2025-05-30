# Generated by Django 5.2 on 2025-05-15 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image_url',
            field=models.ImageField(null=True, upload_to='actors/%Y/%m/%d/ '),
        ),
        migrations.AlterField(
            model_name='director',
            name='image_url',
            field=models.ImageField(null=True, upload_to='directors/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='movies', to='viewer.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.ImageField(null=True, upload_to='movies_posters/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image_url',
            field=models.ImageField(null=True, upload_to='users/'),
        ),
        migrations.CreateModel(
            name='MoviesPremiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=512)),
                ('date_and_time', models.DateTimeField(null=True)),
                ('cinema', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.movie')),
            ],
        ),
    ]
