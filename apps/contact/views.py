from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ContactMessageAPI(APIView):
    def post(self, request):
        data = request.data

        # simple debug response (no DB yet)
        return Response({
            "message": "Data received successfully",
            "data": data
        }, status=status.HTTP_200_OK)