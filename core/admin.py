from itertools import product
from django.contrib import admin
from core.models import Product, Category, ProductImage
from import_export.admin import ImportExportModelAdmin
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail
from django.utils.html import mark_safe


class InlineImage(AdminImageMixin, admin.TabularInline):
    model = ProductImage
    verbose_name = 'Images'
    verbose_name_plural = 'Images'

class ProductAdmin(AdminImageMixin, ImportExportModelAdmin):
    search_fields = ['email', 'product_id', 'name']
    list_display = ['id', 'product_id', 'get_thumbnail', 'name', 'price', 'category', 'date_created', 'date_updated' ]
    list_editable = ['category']
    list_filter = ['category']
    list_display_links = ['product_id']
    inlines = [InlineImage]
    
    def get_thumbnail(self, object):
        # return ProductImage.objects.get(product=object).image_preview
        image= ProductImage.objects.filter(product=object).first()
        return image.image_preview
        # pass
    get_thumbnail.short_description ='Image'
    
    
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'thumbnail','slug', 'parent']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)