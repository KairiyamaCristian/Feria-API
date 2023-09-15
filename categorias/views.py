from rest_framework.viewsets import ModelViewSet
from Categorias.models import categoria
from Categorias.serializers import CategoriaModelSerializer


class categoriasModelViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaModelSerializer
