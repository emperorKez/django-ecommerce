from django.contrib import admin
from  vendor.models import Vendor, VendorProduct
from import_export.admin import ImportExportModelAdmin

# class InlineImage(admin.TabularInline):
#     model = ProductImage

class VendorAdmin(admin.ModelAdmin):
    pass
    search_fields = ['vendor_id', 'user__email', 'shop_name']
    list_display = ['id', 'vendor_id', 'shop_name', 'get_firstname', 'get_lastname', 'vendor_credit', 'get_last_login']
    list_filter = ['user__country',]
    # inlines = ['VendorProductAdmin']
    
    def get_firstname(self, object):
        return object.user.firstname
    get_firstname.admin_order_field = 'user__firstname'
    get_firstname.short_description ='First Name'

    def get_lastname(self, object):
        return object.user.lastname
    get_lastname.admin_order_field = 'user__lastname'
    get_lastname.short_description ='Last Name'

    def get_last_login(self, object):
        return object.user.last_login
    get_last_login.admin_order_field = 'user__email'
    get_last_login.short_description ='last Login'
    
class VendorProductAdmin(ImportExportModelAdmin):
    search_fields = ['product__product_id']
    list_display = ['id', 'get_name', 'get_product_id', 'get_category', 'get_price', 'get_thumbnail', 'get_date_updated']
    list_filter = ['product__category', 'quantity_sold']
    
    def get_name(self, object):
        return object.product.name
    get_name.admin_order_field = 'product__name'
    get_name.short_description ='Name'
    
    def get_product_id(self, object):
        return object.product.product_id
    get_product_id.admin_order_field = 'product__product_id'
    get_product_id.short_description ='Product ID'
    
    def get_category(self, object):
        return object.product.category
    get_category.admin_order_field = 'product__category'
    get_category.short_description ='Category'
    
    def get_price(self, object):
        return object.product.price
    get_price.admin_order_field = 'product__price'
    get_price.short_description ='Price'
    
    def get_thumbnail(self, object):
        return object.product.thumbnail
    get_thumbnail.admin_order_field = 'product__thumbnail'
    get_thumbnail.short_description ='Thumbnail'
    
    def get_date_updated(self, object):
        return object.product.date_updated
    get_date_updated.admin_order_field = 'product__date_updated'
    get_date_updated.short_description ='Date updated'
    



admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorProduct, VendorProductAdmin)
