import keras
import numpy as np
from keras import backend as K
import tensorflow as tf
from tensorflow.python.keras.backend import set_session
from keras.applications import vgg16


def get_session():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.Session(config=config)

K.tensorflow_backend.set_session(get_session())

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
SESS = tf.Session(config=config)
print("model loading")
GRAPH1 = tf.get_default_graph()

set_session(SESS)
# Load the VGG model
VGG_MODEL = vgg16.VGG16(weights="imagenet")