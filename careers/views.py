from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.parsers import MultiPartParser, FormParser

from .models import JobApplication, Job
from .serializers import JobApplicationSerializer, JobSerializer


class JobListView(APIView):

    def get(self, request):
        query = request.GET.get("q", "")
        location = request.GET.get("location", "")

        jobs = Job.objects.all()

        # filter by job title / description
        if query:
            jobs = jobs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )

        # filter by location
        if location:
            jobs = jobs.filter(location__icontains=location)

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)