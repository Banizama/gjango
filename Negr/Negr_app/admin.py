from django.contrib import admin
from .models import Products, Artist, Albums, Instruments, Musician
# Register your models here.

admin.site.register(Products)
admin.site.register(Artist)
admin.site.register(Albums)
admin.site.register(Instruments)
admin.site.register(Musician)
