from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from .models import Job
from .serializers import JobSerializer


class JobListAPI(APIView):

    def get(self, request):

        query = request.GET.get("q", "")
        location = request.GET.get("location", "")

        jobs = Job.objects.filter(status=True)

        # filter by tech stack / title / description
        if query:
            jobs = jobs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tech_stack__icontains=query)
            )

        # filter by location (ignore if "all")
        if location and location.lower() != "all":
            jobs = jobs.filter(location__iexact=location)

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)