from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests


from .word2vec import *
from .forms import *
from django.contrib import messages



def index(request):
    

    return render(request, 'embeddings.html')

def nearestWords(request):
    
    form = wordForm()

    context = {}
    context['view'] = 'index'
    context['form'] = wordForm(request.POST or None)  

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = wordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            word = form.cleaned_data['word']

            closest_embeddings = find_closest_words(request,word,10)
            context['word'] = word
            if len(closest_embeddings) != 0:
                context['closest_embeddings'] = closest_embeddings

            print(closest_embeddings)
    else:
            closest_embeddings = [['papaya', '2.933'], ['guava', '3.136'], ['pineapple', '3.157'], ['avocado', '3.589'], ['pear', '3.698'], ['coconut', '3.759'], ['apricot', '3.792'], ['peach', '3.806'], ['watermelon', '3.935'], ['citrus', '3.969']]
            context['word'] = 'mango'
            context['closest_embeddings'] = closest_embeddings

    return render(request, 'nearest.html', context)





def mathWithWords(request):    

    context = {}
    context['view'] = 'math'
    context['form'] = mathForm2(request.POST or None)  

    # create a form instance and populate it with data from the request:
    form = mathForm2(request.POST or None)
    # check whether it's valid:
    if form.is_valid():

        pos1 = form.cleaned_data['pos1']
        pos2 = form.cleaned_data['pos2']
        neg = form.cleaned_data['neg']

        embed = arithmeticEmbeddings(request,pos1,pos2,neg) 
        
        if len(embed) != 0:
            context['word'] = embed[0]
            context['closest_embeddings'] = embed[1:]



    return render(request, 'math.html', context)

def plotWords(request):    


    context = {}
    context['view'] = 'plot'
    context['form'] = wordForm(request.POST or None)  

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

    return render(request, 'math.html', context)

def firstImage(word):    

    query = "https://pixabay.com/api/?safesearch=true&key=16801238-51413141067eaee8602bc9232&q="+word

    response = requests.get(query)

    data = response.json()

    if len(data['hits'])  == 0 :
        return "http://via.placeholder.com/600x400"
    else:      
        obj = data['hits'][1]
        return obj['webformatURL']



