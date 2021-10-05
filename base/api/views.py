from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.api import serializers
from base.models import Room
from .serializers import RoomcSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomcSerializer(rooms, many=True)
    return Response(serializer.data)
