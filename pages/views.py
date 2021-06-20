from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import View

from .models import Resume, SkillsTag, Portfolio


def resume_view(request):
    resume = Resume.objects.get(pk=1)
    skill_tags = SkillsTag.objects.all().distinct()
    context = {
        "resume": resume,
        "skill_tags": skill_tags,
        "request": request
    }
    print(dir(request))
    return render(request, 'pages/home.html', context)


def portfolio_view(request):
    portfolios = Portfolio.objects.filter(resume_id=1)
    data = serializers.serialize('json', portfolios)
    data = JsonResponse({'data': data}, safe=False)

    return render(request, 'pages/home.html', {'data': data})
