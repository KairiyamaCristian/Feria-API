from django.urls import include, path
from rest_framework import routers
from productores.views import ProductoresModelViewSet

router = routers.DefaultRouter()
router.register("", ProductoresModelViewSet)

urlpatterns = router.urls
