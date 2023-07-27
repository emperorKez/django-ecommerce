from django.db import models
from uuid import uuid4
from shortuuid.django_fields import ShortUUIDField
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from user.models import User
from core.models import Product


def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')  

class Vendor(models.Model):
    vendor_id = ShortUUIDField(unique=True, default=uuid4, editable=False, length= 4, alphabet='abcd1234567890')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False, related_name='user')
    shop_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Shop ID')
    slug = AutoSlugField(populate_from='shop_name', unique_with='vendor_id', slugify=custom_slugify)
    vendor_credit = models.DecimalField(max_digits=6, decimal_places=2, default='0.00', verbose_name='Credit')
    account_number = models.DecimalField(max_digits=10, decimal_places=0)
    bank_name = models.CharField(max_length=50, blank=False, null=True)
    
    class Meta:
            verbose_name_plural = 'Vendors'
        
    def __str__(self):
        return f"{self.shop_name}"
    
class VendorProduct(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor', blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_product', blank=False, null=False)
    quantity_sold = models.SmallIntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Vendor Products'
        ordering = ['-product__date_updated']
        
    def __str__(self):
        return f"{self.vendor.shop_name}"
    

    
  

        