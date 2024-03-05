from django.contrib import admin
from .models import Page


# class CategoryAdmin(admin.ModelAdmin):
#     search_fields = ['name']
#     list_display = ['id', 'name', 'thumbnail','slug', 'parent']


# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title','slug', 'date_created', 'date_updated']
    search_fields = ['name', 'title']
    

admin.site.register(Page, PageAdmin)