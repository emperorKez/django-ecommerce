# Generated by Django 5.0.2 on 2024-03-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='product/<django.db.models.query_utils.DeferredAttribute object at 0x7f9aa0760680>/<django.db.models.query_utils.DeferredAttribute object at 0x7f9aa0adda00>'),
        ),
    ]