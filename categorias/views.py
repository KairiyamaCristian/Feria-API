from rest_framework.viewsets import ModelViewSet
from categorias.models import Categoria
from categorias.serializers import CategoriasModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class categoriasModelViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasModelSerializer
    authentication_classes = [JWTAuthentication]
    
