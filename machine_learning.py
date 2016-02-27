# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:30:17 2016

@author: Maxime
"""

import numpy as np
import random as rd
from Tkinter import *
import Puissance4.py

from sklearn import metrics
from sknn.mlp import Regressor, Layer
from sknn.backend import lasagne
import pickle



class Genetic:
    
    num = Puissance4.longueur * 2
    
    def __init__(self):
        self.nns = []#Current neural networks to be evaluated or mutated
        for i in xrange(Genetic.num):
            self.nns.append(Regressor(layers=[Layer("Sigmoid", units=(Puissance4.longueur * Puissance4.largeur * 2)),Layer("Sigmoid", units=100), Layer("Sigmoid")], learning_rate=0.01, n_iter=1))


    def __init__(self, filename):
        self.nns = []
        for i in xrange(Genetic.num):
            s = s+str(i)
            self.nns.append(pickle.load(open(s, 'rb')))
            s = ""
    

    def select_best(self):#Select the 2 bests nns in the list by testing against an AI, discard the others


    def mutate(self):#Mutate the neural nets we kept
    #Generate 2 different situations
    a = Puissance4()
    #CALL THE IA TO PLAY A COUPLE TIMES AND GET THE SITUATION
    
    #Fit the neural networks to those situations
    
    def save():#Saves the current best networks
        for i,elt in enumerate(self.nns):
            s = 'nn{}.pkl'.format{i}
            pickle.dump(elt, open('nn{}.pkl', 'wb'))


                            
                            
