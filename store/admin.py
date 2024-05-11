from django.contrib import admin
from .models import Genre
from .models import Product
# Register your models here.

admin.site.register(Genre)
admin.site.register(Product)