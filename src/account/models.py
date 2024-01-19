import uuid
from django.db import models
from agrijeune.constants import ENTERPRISE_IMAGE_PATH
from agrijeune.validators import validate_image_extension, valideta_image_size
# Create your models here.



class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "authentications.User",
        on_delete=models.CASCADE,
        verbose_name="User store",
        related_name="store_user",
    )
    name = models.CharField(max_length=255, verbose_name="Nom du magasin")
    address = models.CharField(
        max_length=255, verbose_name="Adresse du magasin", blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=255, verbose_name="Téléphone du magasin"
    )
    logo = models.ImageField(
        upload_to=ENTERPRISE_IMAGE_PATH,
        verbose_name="Logo du magasin",
        blank=True,
        null=True,
        
    )
    description = models.TextField(verbose_name="Description du magasin")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création du magasin"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification du magasin"
    )

    class Meta:
        verbose_name = "Boutique"
        verbose_name_plural = "Boutiques"

    def __str__(self):
        return self.name
