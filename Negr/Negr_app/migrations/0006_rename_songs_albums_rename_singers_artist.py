# Generated by Django 4.2.6 on 2023-10-30 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Negr_app', '0005_alter_songs_year'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Songs',
            new_name='Albums',
        ),
        migrations.RenameModel(
            old_name='Singers',
            new_name='Artist',
        ),
    ]
