from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    return Response({
        "project":"ResumeIQ",
        "messege":"Welcome to ResumeIQ API",
        "status":"Running"
    })
