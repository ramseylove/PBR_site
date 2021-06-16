from django.urls import include, path

from .views import resume_view

urlpatterns = [
    path('', resume_view, name='resume'),
]

