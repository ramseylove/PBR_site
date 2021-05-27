from django.shortcuts import render

from .models import Resume


def resume_view(request):
    resume = Resume.objects.get(pk=1)
    context = {
        "resume": resume
    }
    return render(request, 'pages/home.html', context)