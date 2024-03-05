from django.db import models
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

class Page(models.Model):
    name = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=False)
    slug = AutoSlugField(populate_from='title')
    date_created = models.DateField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateField(auto_now_add=True, verbose_name='Date Updated')
    body = RichTextUploadingField()
    
    class Meta:
        verbose_name_plural = 'Pages'
        
        
    
    def __str__(self):
        return self.name
    


# Create your models here.
