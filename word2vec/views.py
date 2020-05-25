from django.http import HttpResponse


def word2vecView(request):
    return HttpResponse("Hello, world. You're at the word2vec app index.")
