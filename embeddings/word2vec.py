import numpy as np
from scipy import spatial
from sklearn.manifold import TSNE
import matplotlib as mplt
mplt.use('Agg')

embeddings_dict = {}

with open("static/glove.6B.50d.txt", 'r') as f:

    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

def find_closest_words(word,n):
    embedding = embeddings_dict[word]
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))[1:n+1]

def find_closest_embeddings(embedding,n):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))[1:n+1]


def words_plot(words):
    tsne = TSNE(n_components=2, random_state=0)
    vectors = [embeddings_dict[word] for word in words]
    Y = tsne.fit_transform(vectors)
    mplt.pyplot.scatter(Y[:, 0], Y[:, 1])

    for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
        mplt.pyplot.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")

    
    mplt.pyplot.savefig('static/scatter.png')
    mplt.pyplot.clf()
    
def arithmeticEmbeddings(pos,neg):

    posEmbedding = [embeddings_dict[word] for word in pos]
    negEmbedding = [embeddings_dict[word] for word in neg]
    
    word = find_closest_embeddings(sum(posEmbedding) - sum(negEmbedding) , 2)

    return word
