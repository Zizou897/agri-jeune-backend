from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
#from cities_light.models import Country

from .models import ProductCategory, Measure, PaymentMethod, Sectors
from .serializer import (
    ProductCategorySerializer,
    ProductCategoryCreateSerializer,
    MeasureSerializer,
    MeasureCreateSerializer,
    PaymentMethodSerializer,
    PaymentMethodCreateSerializer,
    SectorSerializer,
    SectorCreateSerializer
)
# Create your views here.


class CategoryProductView(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return ProductCategoryCreateSerializer
        return ProductCategorySerializer



class MeasureView(viewsets.ModelViewSet):
    serializer_class = MeasureSerializer
    queryset = Measure.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return MeasureCreateSerializer
        return MeasureSerializer


""" 
class CountryView(APIView):
    def get(self, request):
        pays = Country.objects.all()
        featured_country = Country.objects.get(code2="SN")
        countries = sorted(pays, key=lambda c: c != featured_country)
        serializer_context = {
            "request": request,
        }
        serializer = CountrySerializer(
            instance=countries, many=True, context=serializer_context
        )
        return Response(serializer.data)

        """
class PaymentMethodView(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return PaymentMethodCreateSerializer
        return PaymentMethodSerializer



class SectorView(viewsets.ModelViewSet):
    serializer_class = SectorSerializer
    queryset = Sectors.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return SectorCreateSerializer
        return SectorSerializer


