from rest_framework.serializers import ModelSerializer
from categorias.models import Categoria

class CategoriasModelSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

