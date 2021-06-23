from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import JsonResponse
from django.views.generic import View

from .models import Resume, SkillsTag, Portfolio, PortfolioImages, Skills, Feature
from .forms import ContactForm
from accounts.models import UserProfile


def resume_view(request):
    resume = Resume.objects.select_related('user__userprofile').get(pk=1)
    profile = resume.user.userprofile
    skill_tags = SkillsTag.objects.prefetch_related('tags').all().distinct()
    portfolios = Portfolio.objects.prefetch_related('images').filter(resume=resume)
    skills = Skills.objects.prefetch_related('tag').filter(resume=resume)
    form = ContactForm(request.POST or None)

    if request.is_ajax():
        if form.is_valid():
            from_email = request.POST.get('from_email')
            name = request.POST.get('name')
            subject = 'PBR contact - ' + name
            message = request.POST.get('message')
            email = EmailMessage(
                subject,
                message,
                'dev@atriadev.com',
                ['meyeryan@outlook.com',],
                reply_to=[from_email],
            )
            try:
                email.send()
            except BadHeaderError:
                return JsonResponse({'msg': 'Invalid header found.'})
            return JsonResponse({'msg': 'Email sent successfully'})

    context = {
        "resume": resume,
        "profile": profile,
        "skill_tags": skill_tags,
        "portfolios": portfolios,
        "skills": skills,
        "request": request,
        "form": form,
    }

    return render(request, 'pages/home.html', context)


def portfolio_view(request, pk):
    p = Portfolio.objects.filter(pk=pk)
    features_qs = Feature.objects.filter(portfolio_id=pk)
    pi_qs = PortfolioImages.objects.filter(portfolio_id=pk)

    features = []
    p_images = []

    if request.is_ajax():
        portfolio = {
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'topic': p.topic,
            'portfolio_pic': p.portfolio_pic,
            'problem': p.problem,
            'solution': p.solution,
            'topics': p.get_topics,
        }
        for feature in features_qs:
            f = {
                'title': feature.title,
                'description': feature.description,
                'portfolio': feature.portfolio.id,
                'order': feature.order,
            }
            features.append(f)

        for image in pi_qs:
            item = {
                'alt': image.alt,
                'portfolio_image': image.portfolio_image.url,
                'portfolio': image.portfolio.id,
                'order': image.order,
            }
            p_images.append(image)


    return JsonResponse({'portfolio': portfolio, 'features':features, 'images':p_images})
