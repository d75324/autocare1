from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from autocare.models import Vehicle

class CarsView(ListView):
    model = Vehicle
    template_name = 'cars.html'


class HomeView(TemplateView):
    template_name = 'home.html'

class PricingView(TemplateView):
    template_name = 'pricing.html'
