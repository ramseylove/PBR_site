from django.shortcuts import render

from .models import Resume, SkillsTag


def resume_view(request):
    resume = Resume.objects.get(pk=1)
    skill_tags = SkillsTag.objects.all().distinct()
    context = {
        "resume": resume,
        "skill_tags": skill_tags
    }
    return render(request, 'pages/home.html', context)
