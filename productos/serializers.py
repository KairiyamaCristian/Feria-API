from rest_framework.serializers import ModelSerializer
from productos.models import Productos

class ProductosModelSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = "__all__"

