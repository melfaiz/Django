from django.urls import path

from . import views


urlpatterns = [
    path('', views.ChartView, name='home'),
    path('/delete', views.delPoint, name='delete'),
    path('/predict', views.predict, name='predict'),
]

