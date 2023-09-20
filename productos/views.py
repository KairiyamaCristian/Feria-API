from rest_framework.viewsets import ModelViewSet
from productos.models import Productos
from productos.serializers import ProductosModelSerializer



class ProductosModelViewSet(ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosModelSerializer

    
