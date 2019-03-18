import numpy as np
from tensorflow as tf
from dataset import DataSet
from tensorflow import keras
from keras.datasets import cifra10
from tensorflow.keras import layers

class Network:
    def __init__(self):

        self.model = tf.keras.Sequential()
        #Adding dense layer
        self.model.add(layers.Dense(64, activation='relu', input_shape = (32, )))
        #Repeat
        self.model.add(layers.Dense(64, activation = "relu"))

        #softmax layer
        self.model.add(layers.Dense(10, activation = "softmax"))
    
    def CompileNetwork(self):
        self.model.compile(optimiser = tf.train.AdamOptimiser(0.001),
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])


        
