# Generated by Django 4.2.8 on 2024-01-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/enterprise_logo', verbose_name='Logo du magasin'),
        ),
    ]
