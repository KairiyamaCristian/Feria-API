from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from jwt_auth.serializers import LoginSerializer
from rest_framework.response import Response


@authentication_classes(None)
@permission_classes([AllowAny])
@api_view(["POST"])
def login(request: Request):
    print("en view")
    serializer = LoginSerializer(data=request.data)  # type: ignore
    serializer.is_valid(raise_exception=True)
    return Response(data=serializer.get_tokens(), status=status.HTTP_200_OK)
