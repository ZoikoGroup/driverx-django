from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactMessageSerializer

@api_view(['POST'])
def contact_api(request):
    serializer = ContactMessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()  # 🔥 THIS WAS MISSING
        return Response({"message": "Saved"}, status=201)

    return Response(serializer.errors, status=400)