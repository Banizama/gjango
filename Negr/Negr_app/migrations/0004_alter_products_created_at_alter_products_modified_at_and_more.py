# Generated by Django 4.2.6 on 2023-10-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negr_app', '0003_singers_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='singers',
            name='year',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]
