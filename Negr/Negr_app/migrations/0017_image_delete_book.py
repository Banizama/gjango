# Generated by Django 4.2.6 on 2023-12-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negr_app', '0016_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
