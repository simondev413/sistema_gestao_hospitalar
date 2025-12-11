from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LoginDocView(APIView):

    @swagger_auto_schema(
        operation_description="Login utilizando o sistema nativo do Django REST Framework.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "password"],
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: "Login efetuado com sucesso",
            400: "Credenciais inválidas"
        }
    )
    def post(self, request, *args, **kwargs):
        return Response({"detail": "Use /api/v1/auth/login/ para efetuar login."})

class LogoutDocView(APIView):

    @swagger_auto_schema(
        operation_description="Logout utilizando o sistema nativo do Django REST Framework.",
        responses={200: "Logout efetuado com sucesso"}
    )
    def post(self, request, *args, **kwargs):
        return Response({"detail": "Use /api/v1/auth/logout/ para efetuar logout."})
