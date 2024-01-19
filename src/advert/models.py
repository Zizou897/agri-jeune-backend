import uuid
from django.db import models


from agrijeune.base_enum import ExtendedEnum
from agrijeune.constants import PRODUCT_IMAGE_PATH
# Create your models here.



class ProductType(ExtendedEnum):
    ALL_PRODUCTS = "ALL_PRODUCTS"
    NEW_ADDED_PRODUCTS = "NEW_ADDED_PRODUCTS"
    MOST_SELLING_PRODUCTS = "MOST_SELLING_PRODUCTS"


class ProductStatus(ExtendedEnum):
    PUBLISH = "PUBLISH"
    UNPUBLISH = "UNPUBLISH"
    WAIT = "WAIT"
    REFUSED = "REFUSED"
    ARCHIVED = "ARCHIVED"


class StockStatus(ExtendedEnum):
    IN_STOCK = "IN_STOCK"
    OUT_OF_STOCK = "OUT_OF_STOCK"


class OrderStatus(ExtendedEnum):
    RECEIVED = "RECEIVED"
    PENDING = "PENDING"
    READY_TO_BE_DELIVERED = "READY_TO_BE_DELIVERED"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"






class ProductImage(models.Model):
    is_main = models.BooleanField(default=False, verbose_name="Is main product image")
    image = models.ImageField(
        upload_to=PRODUCT_IMAGE_PATH,
        verbose_name="Product image",
        
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Product image created at"
    )

    class Meta:
        verbose_name = "Product image"
        verbose_name_plural = "Product images"

    def __str__(self):
        return self.image.name


