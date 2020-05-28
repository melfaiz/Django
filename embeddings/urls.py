from django.urls import path
from . import word2vec
from . import views


urlpatterns = [
    path('', views.index, name='embeddings'),
    path('plot', views.plotWords, name='plot'),
    path('math', views.mathWords, name='math'),
]

