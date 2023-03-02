# Generated by Django 3.2.18 on 2023-03-02 09:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_delete_foodtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
