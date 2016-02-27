# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:27:56 2016

@author: thomas
"""

# IA du Puissance4

import Puissance4.py
import numpy as np

# Pour les 7 coups possibles j'obtient la note récursivement

class Arbre:
        
    def __init__(self, value, dernier_jouer, grille):
        self.dernier_joueur = -1
        self.coup_actuel = -1
        self.value = value
        self.fils = []
        self.grille = grille      
        
    def add_son(self,arbre):
        self.fils.append(arbre)
        
    
        




class P4IA:
    
    n = 10
    discount = 0.5
    
    def __init__(self, P):
        self.tree = Arbre(0)
        self.partie = P
        
    def build_tree(self, prof=n, partie, arbre):
        if self.partie.jouer(dernier_coup):
                arbre.value = self.part #n doit être pair
                self.partie.retirer(dernier_coup)
        if n == 0: 
            
        else:
            for i in self.tree.grille.coups_possibles:
                self.tree.append(self.build_tree(n-1))
    

    def build_tree(self, n, arbre):
        if n = 0:
            for i in self.partie.coups_possibles():
                if self.partie.jouer(i):
                    arbre.fils.append(Arbre(i))
            arbre = self.tree

        
    def jouerIA_level(self, p, joueur, n):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

