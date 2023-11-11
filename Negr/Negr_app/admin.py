from django.contrib import admin
from .models import Products, Artist, Albums, Instruments, Musician, Directors, Films, Cart, Country, Admin
# Register your models here.

admin.site.register(Products)
admin.site.register(Artist)
admin.site.register(Albums)
admin.site.register(Instruments)
admin.site.register(Musician)
admin.site.register(Directors)
admin.site.register(Films)
admin.site.register(Cart)
admin.site.register(Country)
admin.site.register(Admin)