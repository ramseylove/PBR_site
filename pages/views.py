from django.shortcuts import render
# from django.contrib.auth import get_user_model

from .models import Resume, SkillsTag, Portfolio, Skills
from accounts.models import UserProfile


def resume_view(request):
    resume = Resume.objects.select_related('user__userprofile').get(pk=1)
    # resume = Resume.objects.get(pk=1)
    profile = resume.user.userprofile
    skill_tags = SkillsTag.objects.prefetch_related('tags').all().distinct()
    portfolio = Portfolio.objects.filter(resume=resume)
    skills = Skills.objects.prefetch_related('tag').filter(resume=resume)
    context = {
        "resume": resume,
        "profile": profile,
        "skill_tags": skill_tags,
        "portfolio": portfolio,
        "skills": skills,
        "request": request
    }
    print(dir(request))
    return render(request, 'pages/home.html', context)
