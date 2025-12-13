from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import BlacklistedToken

@api_view(['POST', 'OPTIONS'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    token = request.auth
    if token:
        BlacklistedToken.objects.create(token=token)
    return Response({"message": "Logout realizado com sucesso."}, status=200)


@api_view(['GET', 'OPTIONS'])
@permission_classes([IsAuthenticated])
def user_data(request):
    user = request.user
    return Response({
        'id': user.id,
        'email': user.email,
        'is_active': user.is_active,
        'tipo': user.tipo,
    }, status=200)
