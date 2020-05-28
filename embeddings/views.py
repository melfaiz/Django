from django.http import HttpResponseRedirect
from django.shortcuts import render

from .word2vec import *
from .forms import *


# import requests

# # get the API KEY here: https://developers.google.com/custom-search/v1/overview
# API_KEY = "AIzaSyDPSUOGUrV49OiB0o6PjRMwGx32-YERKW0"
# # get your Search Engine ID on your CSE control panel
# SEARCH_ENGINE_ID = "013935217407143054564:ksjmxhzhis7"

def index(request):
    
    form = wordForm()

    context = {}
    context['form'] = form 

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = wordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            word = form.cleaned_data['word']

            closest_embeddings = find_closest_words(word,10)        


            context['word'] = word
            context['closest_embeddings'] = closest_embeddings

    return render(request, 'embeddings.html', context)

def plotWords(request):    

    form = wordForm()

    context = {}
    context['form'] = form 

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = wordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            words = form.cleaned_data['word']

            words = words.split(',')

            words_plot(words)

            context['figure'] = 'figure' 

    return render(request, 'embeddings.html', context)



def mathWords(request):    

    form = mathForm()

    context = {}
    context['form'] = form 

    # create a form instance and populate it with data from the request:
    form = mathForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():

        pos = form.cleaned_data['pos']
        pos = pos.split(',')

        neg = form.cleaned_data['neg']
        neg = neg.split(',')

        word = arithmeticEmbeddings(pos,neg)        

        context['word'] = word 

    return render(request, 'math.html', context)



