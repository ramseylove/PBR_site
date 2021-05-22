from django.views.generic import DetailView

from .models import Resume

class HomeView(DetailView):
    template_name = 'pages/home.html'
    model = Resume
    context_object_name = 'resume'