from django.contrib import admin
from core.models import Product, Category, ProductImage
from import_export.admin import ImportExportModelAdmin


class InlineImage(admin.TabularInline):
    model = ProductImage

class ProductAdmin(ImportExportModelAdmin):
    search_fields = ['email', 'product_id', 'name']
    list_display = ['id', 'product_id', 'name', 'category', 'price', 'get_thumbnail', 'date_created']
    list_editable = ['category']
    list_filter = ['category']
    list_display_links = ['product_id']
    inlines = [InlineImage]
    
    def get_thumbnail(self, object):
        return object.InlineImage.thumbnail
    # get_thumbnail.admin_order_field = 'product__thumbnail'
    get_thumbnail.short_description ='Thumbnail'
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'thumbnail','slug', 'parent']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)