from django.contrib import admin
from  vendor.models import Vendor, VendorProduct

# class InlineImage(admin.TabularInline):
#     model = ProductImage

class VendorAdmin(admin.ModelAdmin):
    search_fields = ['vendor_id', 'user__email', 'shop_name']
    list_display = ['id', 'vendor_id', 'shop_name', 'user__firstname', 'user__lastname', 'vendor_credit', 'user__last_login']
    list_filter = ['user__country',]
    inlines = ['VendorProductAdmin']
    
class VendorProductAdmin(admin.ModelAdmin):
    search_fields = ['product__product_id']
    list_display = ['id', 'product__name', 'product__product_id', 'product__category', 'product__price', 'product__tumbnail', 'product__date_updated']
    list_filter = ['product__category', 'quantity_sold']


admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorProduct, VendorProductAdmin)
