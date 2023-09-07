from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

DEFAULT_AUTH_FAIL_DETAIL = "Credenciales invalidas."


class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def get_user(self) -> User:
        try:
            user = User.objects.get(username=self.validated_data["user"])  # type: ignore
        except User.DoesNotExist:
            raise AuthenticationFailed(detail=DEFAULT_AUTH_FAIL_DETAIL)
        return user

    def get_tokens(self) -> dict[str, str]:
        user = self.get_user()
        if not user.check_password(self.validated_data["password"]):  # type: ignore
            raise AuthenticationFailed(detail=DEFAULT_AUTH_FAIL_DETAIL)
        tokens = RefreshToken.for_user(user)
        return {"access_token": str(tokens.access_token), "refresh_token": str(tokens)}  # type: ignore
