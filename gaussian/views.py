from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Point


class ChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Point.objects.all()
        return context