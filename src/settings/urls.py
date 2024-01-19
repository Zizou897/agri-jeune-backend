from django.urls import path

from rest_framework.routers import DefaultRouter
from settings.views import (
    CategoryProductView,
    MeasureView,
    SectorView,
    PaymentMethodView,
   
)


router = DefaultRouter()

router.register("category-product", CategoryProductView, basename="category-product")
router.register("payment-method", PaymentMethodView, basename="payment-method")
router.register("measure", MeasureView, basename="measure")
router.register("sector", SectorView, basename="sector")


urlpatterns = [
    #path("countries/", CountryView.as_view(), name="countries"),
]

urlpatterns += router.urls