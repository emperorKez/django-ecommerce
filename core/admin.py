# from datetime import time
# import datetime
from django.contrib import admin
from core.models import Product, Category, ProductImage
from import_export.admin import ImportExportModelAdmin
# from time import strftime

# def date_format(obj):
#     return obj.strftime('%d-%m-%Y')
# # def date_format(self, obj):
# #     return obj.date_created.strftime('%d/%m/%Y')
# # date_format.admin_order_field = 'date_created'
# # time_seconds.short_description = 'Precise Time'

class InlineImage(admin.TabularInline):
    model = ProductImage

class ProductAdmin(ImportExportModelAdmin):
    search_fields = ['email', 'product_id', 'name']
    list_display = ['product_id', 'name', 'description', 'category', 'date_created']
    list_editable = ['category']
    list_filter = ['category']
    list_display_links = ['product_id']
    inlines = [InlineImage]
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'description', 'tumbnail', 'children']
    list_editable = ['name', 'description', 'tumbnail', 'children']
    list_display_links = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)