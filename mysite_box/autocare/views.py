from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from autocare.models import Vehicle

class CarsView(ListView):
    model = Vehicle
    template_name = 'cars.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # if self.request.user.groups.filter(name='Mecanicos').exists():
        if self.request.user.is_anonymous:
            return queryset.none()
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset



class HomeView(TemplateView):
    template_name = 'home.html'

class PricingView(TemplateView):
    template_name = 'pricing.html'
