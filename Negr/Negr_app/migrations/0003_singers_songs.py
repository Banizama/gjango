# Generated by Django 4.2.6 on 2023-10-29 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Negr_app', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('poster', models.ImageField(upload_to='static/images')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Negr_app.singers')),
            ],
        ),
    ]