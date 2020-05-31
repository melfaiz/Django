from django.urls import path
from . import word2vec
from . import views


urlpatterns = [
    path('', views.index, name='embeddings'),
    path('nearsetWords', views.nearestWords, name='nearest'),
    path('mathWithWords', views.mathWithWords, name='math'),
]

