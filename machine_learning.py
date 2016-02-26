# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:30:17 2016

@author: Maxime
"""

import numpy as np
import random as rd
from Tkinter import *
import Puissance4.py

#On associe à chaque état + coup une récompense R(état)
#On apprendre R(état) + gamma*R(meilleur tat suivant) + j^2 R(meilleur etat suivant)...


class ValueIteration:
    def __init__():
        self.v = [[rd.random(1.)]*Puissance4.longueur] * Puissance4.largeur
    
