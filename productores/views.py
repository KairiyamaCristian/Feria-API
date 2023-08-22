from rest_framework.viewsets import ModelViewSet
from productores.models import Productor
from productores.serializers import ProductorModelSerializer


class ProductoresModelViewSet(ModelViewSet):
    queryset = Productor.objects.all()
    serializer_class = ProductorModelSerializer
