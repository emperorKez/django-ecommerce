from django.contrib import admin
from core.models import Product, Category, ProductImage
from import_export.admin import ImportExportModelAdmin


class InlineImage(admin.TabularInline):
    model = ProductImage

class ProductAdmin(ImportExportModelAdmin):
    search_fields = ['email', 'product_id', 'name']
    list_display = ['id', 'product_id', 'name', 'category', 'date_created']
    list_editable = ['category']
    list_filter = ['category']
    list_display_links = ['product_id']
    inlines = [InlineImage]
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'tumbnail','slug', 'parent']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)