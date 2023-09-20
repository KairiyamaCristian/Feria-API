from django.urls import include, path
from rest_framework import routers
from categorias.views import categoriasModelViewSet

router = routers.DefaultRouter()
router.register("", categoriasModelViewSet)

urlpatterns = router.urls
