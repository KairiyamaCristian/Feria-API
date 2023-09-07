from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from jwt_auth.serializers import LoginSerializer
from rest_framework.response import Response


@authentication_classes(None)
@api_view(["POST"])
def login(request: Request):
    serializer = LoginSerializer(data=request.data)  # type: ignore
    serializer.is_valid(raise_exception=True)
    return Response(data=serializer.get_tokens(), status=status.HTTP_200_OK)


@api_view(["POST"])
def refresh(request: Request):
    serializer = LoginSerializer(data=request.data)  # type: ignore
    serializer.is_valid(raise_exception=True)
    return Response(data=serializer.get_tokens(), status=status.HTTP_200_OK)
