from rest_framework.viewsets import ModelViewSet
from productores.models import Productor
from productores.serializers import ProductorModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductoresModelViewSet(ModelViewSet):
    queryset = Productor.objects.all()
    serializer_class = ProductorModelSerializer
    authentication_classes = [JWTAuthentication]
    
