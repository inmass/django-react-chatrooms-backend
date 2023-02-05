from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RoomSerializer
from user.models import Room

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRooms(request):

    # get all available rooms
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRoom(request):

    # create a new room
    try:
        Room.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        data = {
            'detail': 'Room created successfully'
        }
    except:
        data = {
            'detail': 'Room creation failed'
        }

    return Response(data)