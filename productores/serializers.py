from rest_framework.serializers import ModelSerializer
from productores.models import Productor


class ProductorModelSerializer(ModelSerializer):
    class Meta:
        model = Productor
        fields = "__all__"
