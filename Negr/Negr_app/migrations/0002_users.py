# Generated by Django 4.2.6 on 2023-10-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
