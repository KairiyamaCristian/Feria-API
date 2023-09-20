"""
URL configuration for FeriaVirtual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from productores.urls import urlpatterns as productores_router
from categorias.urls import urlpatterns as categorias_router
from categorias.urls import urlpatterns as productos_router

from jwt_auth.urls import urlpatterns as auth_router

api_router = [
    path(r"categorias/", include(categorias_router)),
    path(r"productores/", include(productores_router)),
    path(r"productos/", include(productos_router)),
    path(r"auth/", include(auth_router)),
]


urlpatterns = [
    path(r"api/", include(api_router)),
]
