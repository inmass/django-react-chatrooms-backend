from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import UserSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

@api_view(['POST'])
def registerUser(request):
    data = request.data

    username = data['username']
    password = data['password']
    password_confirmation = data['password_confirmation']
    print(username, password, password_confirmation)
        

    return Response(data)

@api_view(['GET'])
def getRoutes(request):

    routes = {
        'tokens':'api/token/',
        'refresh':'api/token/refresh/',
    }

    return Response(routes)