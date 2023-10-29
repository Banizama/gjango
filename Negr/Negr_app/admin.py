from django.contrib import admin
from .models import Products, Singers, Songs
# Register your models here.

admin.site.register(Products)
admin.site.register(Singers)
admin.site.register(Songs)