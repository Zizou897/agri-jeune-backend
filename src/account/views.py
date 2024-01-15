from rest_framework.viewsets import ModelViewSet

from .filters import StoreFilter
from .models import Store
from .serializer import StoreSerializer, StoreCreateSerializer
# Create your views here.


class StoreView(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filterset_class = StoreFilter

    def get_serializer_class(self):
        if self.action in ["create", "put", "patch"]:
            return StoreCreateSerializer
        return StoreSerializer
