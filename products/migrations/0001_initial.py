# Generated by Django 5.0.6 on 2024-06-01 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Color',
                'verbose_name_plural': 'Product Colors',
            },
        ),
        migrations.CreateModel(
            name='ProductManufactureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='manufacture/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Color',
                'verbose_name_plural': 'Product Colors',
            },
        ),
        migrations.CreateModel(
            name='ProductSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Size',
                'verbose_name_plural': 'Product Sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product Tag',
                'verbose_name_plural': 'Product Tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='products/')),
                ('name', models.CharField(max_length=225)),
                ('long_description', models.TextField()),
                ('short_description', models.CharField(max_length=225)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('sku', models.CharField(max_length=10, unique=True)),
                ('count', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='products', to='products.productcategorymodel')),
                ('colors', models.ManyToManyField(related_name='products', to='products.productcolormodel')),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.productmanufacturemodel')),
                ('sizes', models.ManyToManyField(related_name='products', to='products.productsizemodel')),
                ('tags', models.ManyToManyField(related_name='products', to='products.producttagmodel')),
            ],
            options={
                'verbose_name': 'Product Color',
                'verbose_name_plural': 'Product Colors',
            },
        ),
    ]
