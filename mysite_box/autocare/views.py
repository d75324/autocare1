from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class PricingView(TemplateView):
    template_name = 'pricing.html'
