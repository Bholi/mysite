from .models import Education
from .serializer import EducationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def educationView(reponse):
    data = Education.objects.all()
    serializer = EducationSerializer(data,many=True)
    return Response(serializer.data)
