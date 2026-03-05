from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer


class JobListAPI(APIView):
    def get(self, request):
        jobs = Job.objects.filter(status=True)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)