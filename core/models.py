from email.policy import default
from random import choice
import autoslug
from django.db import models
from uuid import uuid4
from shortuuid.django_fields import ShortUUIDField
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from sorl.thumbnail import ImageField
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


def custom_slugify(value):
    return default_slugify(value).replace(' ', '-')  

class Product(models.Model):
    product_id = ShortUUIDField(unique=True, default=uuid4, editable=False, length= 10, alphabet='1234567890')
    name = models.CharField(max_length=150, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique_with='product_id', slugify=custom_slugify)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    quantity = models.DecimalField(max_digits=3, decimal_places=0)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=False, null=False, related_name='category')
    # short_description = models.TextField(blank=False, null=False)
    description = RichTextUploadingField()
    date_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateField(auto_now_add=True, verbose_name='Date Updated')
        
    def __str__(self):
        return f"{self.name}"
    
    
class Category(models.Model):
    # my_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=75, blank=False, null=False, editable=True,)
    parent = models.ForeignKey('Category', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='parent_category')
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='category', editable=True, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique_with='id', slugify=custom_slugify)
    date_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateField(auto_now=True, verbose_name='Date Updated')
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        
        
    def __str__(self):
        return f"{self.name}"
    
IMAGE_TYPE = (('thumbnail', 'Thumbnail'), ('other', 'Other'))

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    image = ImageField(upload_to=f'products/', null=False, blank=False, max_length=100)
    type = models.CharField(max_length=25, choices=IMAGE_TYPE, default='thumbnail')
    
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""
    
    def __str__(self):
        return f"{self.image}"
    
    
class ProductVariation(models.Model):
    pass
  

        