from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

DEFAULT_AUTH_FAIL_DETAIL = "Credenciales invalidas."


class LoginSerializer(serializers.Serializer):
    user_model = get_user_model()
    user: user_model = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def get_user(self):
        try:
            user = self.user_model.objects.get(username=self.validated_data["user"])  # type: ignore
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(detail=DEFAULT_AUTH_FAIL_DETAIL)
        return user

    def get_tokens(self) -> dict[str, str]:
        user = self.get_user()
        if not user.check_password(self.validated_data["password"]):  # type: ignore
            raise AuthenticationFailed(detail=DEFAULT_AUTH_FAIL_DETAIL)
        tokens = RefreshToken.for_user(user)
        return {"access_token": str(tokens.access_token), "refresh_token": str(tokens)}  # type: ignore
