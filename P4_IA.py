# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:27:56 2016

@author: thomas
"""

# IA du Puissance4

import random as rd
import numpy as np

# Pour les 7 coups possibles j'obtient la note récursivement

def calculer_score(arbre):
    if len(arbre.fils) != 0:
        for elt in arbre.fils:
            calculer_score(elt)
        coup_max = -2
        for elt in arbre.fils:
            if elt.value > coup_max:
                coup_max = elt.value
        arbre.value = -coup_max*P4IA.discount


class Arbre:
        
    def __init__(self, coup, value):
        self.value = value
        self.coup = coup
        self.fils = []
        
    def add_son(self,coup,value):
        self.fils.append(Arbre(coup,value))
        
def afficher(a):
    for elt in a.fils:
        afficher(elt)
    print a.coup, a.value
        




class P4IA:
    
    n = 10
    discount = 0.5
    
    def __init__(self, P, joueur):
        self.tree = Arbre(-1,0)
        self.partie = P
        self.joueur = joueur
        
    def build_tree(self, n, arbre):#n should be even when we call build_tree the first time.
        if (n == 0):
            for elt in self.partie.coups_possibles():
                if (self.partie.jouer(elt, self.joueur)):
                    arbre.add_son(elt,1)
                else:
                    arbre.add_son(elt,0)
                self.partie.retirer(elt)
        else:
            if (n%2 == 0):
                j = self.joueur
            else:
                j = int(self.joueur - (-1)**self.joueur)
            if (j == self.joueur):
                par = 1
            else:
                par = -1
            for elt in self.partie.coups_possibles():
                if (self.partie.jouer(elt, j)):
                    arbre.add_son(elt, par)
                else:
                    arbre.fils.append(self.build_tree(n-1, Arbre(elt,0)))
                self.partie.retirer(elt)
        return arbre

    def build_tree2(self, n):
        self.tree = self.build_tree(n , Arbre(-1,0))

    def update_scores(self):
        calculer_score(self.tree)

    def coup_IA(self,n):
        self.build_tree2(n)
        self.update_scores()
        coup_max = -10
        coup_a_jouer = []
        for elt in self.tree.fils:
            if elt.value > coup_max + 0.001:
                coup_a_jouer = [elt.coup]
                coup_max = elt.value
            elif (elt.value >= coup_max):
                coup_a_jouer.append(elt.coup)
        l =len(coup_a_jouer)
        print l
        if (l>1):
            r=rd.randint(0,l-1)
            return coup_a_jouer[r]
        else:
            return coup_a_jouer[0]




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

