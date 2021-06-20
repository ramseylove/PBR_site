from django.urls import path

from .views import resume_view, portfolio_view

urlpatterns = [
    path('', resume_view, name='resume'),
    path('portfolio/', portfolio_view, name='portfolio')
]

