# Generated by Django 5.0.2 on 2024-03-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_productimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/<django.db.models.query_utils.DeferredAttribute object at 0x7fa15c4d0680>/<django.db.models.query_utils.DeferredAttribute object at 0x7fa15c4ab590>'),
        ),
    ]
