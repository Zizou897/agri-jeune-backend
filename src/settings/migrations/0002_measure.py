# Generated by Django 4.2.8 on 2024-01-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Measure name')),
                ('short_name', models.CharField(max_length=255, verbose_name='Measure short name')),
                ('language_key', models.CharField(blank=True, max_length=255, null=True, verbose_name='Measure language key')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Measure created at')),
            ],
            options={
                'verbose_name': 'Measure',
                'verbose_name_plural': 'Measures',
            },
        ),
    ]
