# Generated by Django 4.2.8 on 2024-01-08 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0003_alter_user_gender_alter_user_profil_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]