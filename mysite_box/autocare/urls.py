from django.urls import path
from .views import CarsView, HomeView, PricingView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('cars/', CarsView.as_view(), name='cars'),
]
