import numpy as np
from scipy import spatial
from sklearn.manifold import TSNE


from django.contrib import messages
embeddings_dict = {}

with open("static/glove.6B.100d.txt", 'r') as f:
    print("LOADING THE FILE")
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

def find_closest_words(request,word,n):
    if word in embeddings_dict.keys():
        embedding = embeddings_dict[word]
        sorted_array = sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))[1:n+1]
        return [[word, '{:.3f}'.format(spatial.distance.euclidean(embeddings_dict[word], embedding))] for word in sorted_array]
    else:
        messages.warning(request, 'No such key!')
        return []

def find_closest_embeddings(embedding,n):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))[1:n+1]

def arithmeticEmbeddings(request,pos1,pos2,neg):

    if pos1 not in embeddings_dict.keys() or pos2 not in embeddings_dict.keys() or neg not in embeddings_dict.keys():
        messages.warning(request, 'No such words in dict')
        return []
    else:
        word = find_closest_embeddings(embeddings_dict[pos1] + embeddings_dict[pos2] - embeddings_dict[neg] , 7)

        return word

def words_plot(words):

    labels = []
    tokens = []

    for word in words:
        tokens.append(embeddings_dict[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=3000, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    mplt.pyplot.figure(figsize=(7, 7)) 
    for i in range(len(x)):
        mplt.pyplot.scatter(x[i],y[i])
        mplt.pyplot.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(15, 4),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')


    mplt.pyplot.savefig('static/scatter.png')
    mplt.pyplot.clf()
    




