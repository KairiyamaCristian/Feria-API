from django.urls import include, path
from rest_framework import routers
from productos.views import ProductosModelViewSet

router = routers.DefaultRouter()
router.register("", ProductosModelViewSet)

urlpatterns = router.urls
