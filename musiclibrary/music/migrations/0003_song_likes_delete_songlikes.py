# Generated by Django 4.0.2 on 2022-02-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_songlikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='SongLikes',
        ),
    ]
