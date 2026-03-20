from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactMessageSerializer

class ContactMessageAPI(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Saved"}, status=201)
        
        return Response(serializer.errors, status=400)