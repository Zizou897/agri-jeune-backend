# Generated by Django 4.2.8 on 2024-01-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('AGRIPRENEUR', 'Agripreneur'), ('MERCHANT', 'Commerçant'), ('CLIENT', 'client'), ('USER', 'Utlisateur')], max_length=255, null=True, verbose_name='sexe'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profil_type',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='USER', max_length=255, verbose_name='profil type'),
        ),
    ]
