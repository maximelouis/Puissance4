# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:27:56 2016

@author: thomas
"""

# IA du Puissance4

import random as rd
import numpy as np

# Pour les 7 coups possibles j'obtient la note récursivement

def calculer_score_bis(arbre):
    # Principe du minmax: si un -1 est présent après le tour de B 
    #(coup gagnant pour B), il remonte. S'il n'y a pas de -1, on fait la
    # moyenne et on la fait remonter (éventuellement réduite par le facteur
    # discount). Après un tour de A on inverse tout : s'il y a un 1 il remonte
    # sinon on moyenne.
    discount = 0.8    
    if len(arbre.fils) != 0:
        for elt in arbre.fils:
            calculer_score_bis(elt)
        if (arbre.depth%2 == 0):
            if (tree_max(arbre.fils) == 1):
                arbre.value = tree_max(arbre.fils)
            else:
                arbre.value = tree_moy(arbre.fils)*discount
        else:
            if (tree_min(arbre.fils) == -1):
                arbre.value = tree_min(arbre.fils)
            else:
                arbre.value = tree_moy(arbre.fils)*discount

def calculer_score(arbre):
    if len(arbre.fils) != 0:
        for elt in arbre.fils:
            calculer_score(elt)
        if (arbre.depth%2 == 0):
            arbre.value = tree_max(arbre.fils)
        else:
            arbre.value = tree_min(arbre.fils)

def tree_moy(l):
    if (l == []):
        return 0
    total = 0
    for elt in l:
        total += elt.value
    return float(total)/len(l)

def tree_min(l):
    mine = 2
    for elt in l:
        if elt.value < mine:
            mine = elt.value
    return mine
        
    
def tree_max(l):
    maxe= -2
    for elt in l:
        if elt.value > maxe:
            maxe = elt.value
    return maxe
    

class Arbre:
        
    def __init__(self, coup, value, depth):
        self.value = value
        self.coup = coup
        self.depth = depth
        self.fils = []
        
    def add_son(self,coup,value):
        self.fils.append(Arbre(coup,value,self.depth + 1))
        



def afficher(a):
    compteur = 0
    l = []
    l.append(a)
    depth = a.depth
    s = ""
    while (len(l)>0):
        f = l.pop(0)
        if (f.depth != depth):
            print s
            print "new line"
            s = ""
            depth = f.depth
        s += ';' + str(f.value)
        compteur += 1
        for elt in f.fils:
            l.append(elt)
    print s
    print compteur




class P4IA:
    
    n = 10
    discount = 0.5
    
    def __init__(self, P, joueur):
        self.tree = Arbre(-1,0,0)
        self.partie = P
        self.joueur = joueur
        
    def build_tree(self, n, arbre):#n should be even when we call build_tree the first time.
        if (n == 1):
            for elt in self.partie.coups_possibles():
                if (self.partie.jouer(elt, int(self.joueur - (-1)**self.joueur))):
                    arbre.add_son(elt,-1)
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
                    arbre.fils.append(self.build_tree(n-1, Arbre(elt,0,arbre.depth + 1)))
                self.partie.retirer(elt)
        return arbre

    def build_tree2(self, n):
        self.tree = self.build_tree(n , Arbre(-1,0,0))

    def update_scores(self):
        calculer_score_bis(self.tree)

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
        if (l>1):
            r=rd.randint(0,l-1)
            print coup_a_jouer[r]
            self.partie.jouer(coup_a_jouer[r],self.joueur,True)
        else:
            print coup_a_jouer[0]
            self.partie.jouer(coup_a_jouer[0],self.joueur,True)





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

