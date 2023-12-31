# Generated by Django 4.2.3 on 2023-07-27 02:29

import autoslug.fields
import core.models
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='category')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=core.models.custom_slugify, unique_with=('id',))),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now=True, verbose_name='Date Updated')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parent_category', to='core.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', editable=False, length=10, max_length=10, prefix='', unique=True)),
                ('name', models.CharField(max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=core.models.custom_slugify, unique_with=('product_id',))),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateField(auto_now_add=True, verbose_name='Date Updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='core.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='core.productimage'),
        ),
    ]
