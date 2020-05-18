from django.contrib import admin
from backend.models import News, Product

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)
admin.site.register(Product, ProductAdmin)