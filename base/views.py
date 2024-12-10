from .models import Profile
from .serializer import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getProfile(request):
    data = Profile.objects.all()
    dataserializer = ProfileSerializer(data,many=True)
    return Response(dataserializer.data)
