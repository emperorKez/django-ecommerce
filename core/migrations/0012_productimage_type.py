# Generated by Django 5.0.2 on 2024-03-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='type',
            field=models.CharField(choices=[('thumbnail', 'Thumbnail'), ('other', 'Other')], default='thumbnail', max_length=25),
        ),
    ]
