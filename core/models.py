from django.db import models
from uuid import uuid4
from shortuuid.django_fields import ShortUUIDField


class Product(models.Model):
    product_id = ShortUUIDField(primary_key=True, unique=True, default=uuid4, editable=False, length= 10, alphabet='1234567890')
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=False, null=False, related_name='category')
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    images = models.ForeignKey('ProductImage', on_delete=models.DO_NOTHING, blank=False, null=False, related_name='images')
    date_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateField(auto_now_add=True, verbose_name='Date Updated')
    
    # class Meta:
    #     ordering = ['-date_created']
        
    def __str__(self):
        return f"{self.name}"
    
class Category(models.Model):
    # my_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75, blank=False, null=False)
    description = models.CharField(max_length=75, blank=True, null=True)
    tumbnail = models.ImageField(upload_to='category', editable=True)
    children = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='child')
    date_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return f"{self.name}"
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product', editable=True, blank=True, null=True)
    

        