from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import View

from .models import Resume, SkillsTag, Portfolio, Skills
from accounts.models import UserProfile


def resume_view(request):
    resume = Resume.objects.select_related('user__userprofile').get(pk=1)
    profile = resume.user.userprofile
    skill_tags = SkillsTag.objects.prefetch_related('tags').all().distinct()
    portfolios = Portfolio.objects.prefetch_related('images').filter(resume=resume)
    skills = Skills.objects.prefetch_related('tag').filter(resume=resume)
    context = {
        "resume": resume,
        "profile": profile,
        "skill_tags": skill_tags,
        "portfolios": portfolios,
        "skills": skills,
        "request": request
    }
    print(dir(request))
    return render(request, 'pages/home.html', context)


def portfolio_view(request):
    portfolios = Portfolio.objects.filter(resume_id=1)
    data = serializers.serialize('json', portfolios)
    data = JsonResponse({'data': data}, safe=False)

    return render(request, 'pages/home.html', {'data': data})
