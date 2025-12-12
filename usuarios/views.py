from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken

@api_view(['POST'])
def logout_view(request):
    try:
        # Pega o token atual do usuário e adiciona na blacklist
        token = request.auth
        if token:
            BlacklistedToken.objects.create(token=token)
        return Response({"message": "Logout realizado com sucesso."}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
def user_data(request):
    try:
        user = request.user
        email = user.email
        _id = user.id
        is_active = user.is_active
        tipo = user.tipo
        context = {
            'id':_id,
            'email':email,
            'is_active':is_active,
            'tipo':tipo
        }
        return Response(context,status=200)
    except Exception as e:
        return Response({'Error':str(e)},status=400)