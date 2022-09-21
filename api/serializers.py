from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from pages.models import Resume, Skills, WorkExperience, Education, Portfolio


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        depth = 1
        model = Resume


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        depth = 1
        model = Skills


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = WorkExperience


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Education


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Portfolio