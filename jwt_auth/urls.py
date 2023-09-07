from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from jwt_auth.views import login

urlpatterns = [path("login/", login), path("refresh/", TokenRefreshView.as_view())]
