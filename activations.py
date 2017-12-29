import numpy as np

'''
This file supplies the activation functions for the neural network. Each activation class
has an activate method, which calculates the activation for forwards propagation, and a 
gradient method, which calculates the gradient for backpropagation.
'''

#Sigmoid Activation
class Sigmoid:

    #Elementwise sigmoid function on the input
    def activate(self, x):
        s = 1 / (1 + np.exp(-x))
        return s

    #Elementwise sigmoid gradient
    def gradient(self, x):
        grad = x * (1 - x)
        return grad

#Rectified Linear Unit activation
class ReLU:

    #Elemetwise ReLU function on input
    def activate(self, x):
        s = np.maximum(0, x)
        return s

    #Elementwise ReLU gradient
    def gradient(self, x):
        grad = (x != 0)
        return grad