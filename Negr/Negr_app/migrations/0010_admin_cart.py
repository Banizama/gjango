# Generated by Django 4.2.6 on 2023-11-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negr_app', '0009_remove_films_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(default='admin', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
