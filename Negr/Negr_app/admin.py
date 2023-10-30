from django.contrib import admin
from .models import Products, Artist, Albums
# Register your models here.

admin.site.register(Products)
admin.site.register(Artist)
admin.site.register(Albums)