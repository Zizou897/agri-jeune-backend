# Generated by Django 4.2.8 on 2024-01-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product category name')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Product category slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/product_categories', verbose_name='Product category image')),
                ('language_key', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product category language key')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Product category created at')),
                ('publish', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
    ]