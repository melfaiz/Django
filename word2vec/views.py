from django.http import HttpResponse
from django.shortcuts import render


def word2vecView(request):
    return render(request, 'word2vec.html')
