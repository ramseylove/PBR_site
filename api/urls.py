from django.urls import path
from .views import resume_view

urlpatterns = [path('resume/<int:pk>/', resume_view.as_view())]