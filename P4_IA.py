# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:27:56 2016

@author: thomas
"""

# IA du Puissance4

import Puissance4_jeu as PJeu
import numpy as np

# Pour les 7 coups possibles j'obtient la note récursivement

class Arbre:
        
    def __init__(self, value):
        self.value = value
        self.fils = []
        
    def add_son(self,i):
        self.fils.append(Arbre(i))
        
    def afficher(self):
        for elt in self.fils:
            elt.afficher()
        print self.value
        




class P4IA:
    
    n = 10
    discount = 0.5
    
    def __init__(self, P, joueur):
        self.tree = Arbre((-1,0))
        self.partie = P
        self.joueur = joueur
        
    def build_tree(self, n, arbre):#n should be even when we call build_tree the first time.
        if (n == 0):
            for elt in self.partie.coups_possibles():
                if (self.partie.jouer(elt, self.joueur)):
                    arbre.add_son((elt,self.joueur))
                else:
                    arbre.add_son((elt,0))
                self.partie.retirer(elt)
        else:
            if (n%2 == 0):
                j = self.joueur
            else:
                j = self.joueur - (-1)**self.joueur
            for elt in self.partie.coups_possibles():
                if (self.partie.jouer(elt, j)):
                    arbre.add_son((elt,j))
                else:
                    arbre.add_son(self.build_tree(n-1, Arbre((elt,0))))
                self.partie.retirer(elt)
            
    

        

a = PJeu.Puissance4()
s = P4IA(a, 1)
s.build_tree(4,s.tree)
s.tree.afficher()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

