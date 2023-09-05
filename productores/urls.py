from django.urls import include, path
from rest_framework import routers
from productores import views

router = routers.DefaultRouter()
router.register("productores", views.ProductoresModelViewSet)
