from django.urls import path

from .views import HomeView

urlpatterns = [
    path('home/<int:pk>', HomeView.as_view(), name='home'),
]

