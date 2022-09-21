from pages.models import Resume
from rest_framework import generics
from .serializers import ResumeSerializer, SkillsSerializer, EducationSerializer, PortfolioSerializer, WorkSerializer
from accounts.models import UserProfile
from pages.models import Resume

class resume_view(generics.RetrieveAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

   