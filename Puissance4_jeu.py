# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:30:17 2016

@author: Maxime
"""

import numpy as np
import random as rd
from Tkinter import *
import P4_IA as IA

def convert_coordinates(i, j):#Converti les coordonnées dans le tableau en coordonnée sur la fenêtre
    return Puissance4.H - (Puissance4.hauteur-i) * Puissance4.H / Puissance4.hauteur, j * Puissance4.L / Puissance4.longueur



class Puissance4(Tk):
    
    L = 300 #Largeur de la fenêtre
    longueur = 7
    hauteur = 6
    H = (hauteur*1./longueur) * L
    n = 4
    
#    def callback(self, event):
#        self.frame.focus_set()
#        x = event.x
#        x = int(x*Puissance4.longueur/Puissance4.L)
#        self.jouer(x,1)
#        ARTIF = IA.P4IA(self, 2)
#        joueur = 2
#        coup = ARTIF.coup_IA()
#        self.jouer(coup, 2)

    
    def __init__(self):
        Tk.__init__(self)
        self.matrice_J1 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.matrice_J2 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.tableau_jeu = np.zeros(Puissance4.longueur)
        self.frame = Frame(self, width=Puissance4.L, height=Puissance4.H)
        self.canvas = Canvas(self, width=Puissance4.L, height=Puissance4.H, bg="white")
        self.frame.pack()
        self.canvas.pack()
        joueur = 1
        #while True:
         #   print joueur
          #  IAL = IA.P4IA(self,joueur)
           # self.jouer(IAL.coup_IA(4),joueur, True)
            #joueur = int(joueur - (-1)**joueur)
    
    def reset(self):
        self.matrice_J1 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.matrice_J2 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.tableau_jeu = np.zeros(Puissance4.longueur)
        self.frame = Frame(self, width=Puissance4.L, height=Puissance4.H)
        self.canvas = Canvas(self, width=Puissance4.L, height=Puissance4.H, bg="white")
        self.canvas.pack()

    
    def jouer(self,poz,joueur,display=False):
        if (np.sum(self.tableau_jeu) == Puissance4.longueur * Puissance4.hauteur):
            raise IndexError("Egalite")
        if (poz < 0) or (poz >= Puissance4.longueur):
            raise ValueError("vous visez à coté")
        elif(self.tableau_jeu[poz] == Puissance4.hauteur):
            raise ValueError("La colonne est pleine")
        else:
            high = int(self.tableau_jeu[poz])
            if (joueur == 1):
                self.matrice_J1[high, poz] = 1
            elif (joueur == 2):
                self.matrice_J2[high, poz] = 1
            self.tableau_jeu[poz] = high+1
            if display:
                self.afficher()
            if self.coup_gagnant(high, poz,joueur):
                return True
        return False

    def coup_gagnant(self, x, y, joueur):
        if (joueur == 1):
            matrice_test = self.matrice_J1
        elif (joueur == 2):
            matrice_test = self.matrice_J2
            
        #print matrice_test        
        tableau = np.zeros(4)
        
        #Vers le haut
        i = x
        j = y        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[0] += 1
            i += 1
        #Vers le bas
        i = x-1
        j = y        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[0] += 1
            i -= 1
        
        if (tableau[0] >= Puissance4.n):
            #print("le joueur {} a gagné".format(joueur))
            return True
        
        #Vers le haut à gauche
        i = x
        j = y       
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[1] += 1
            i += 1
            j -= 1
        #Vers le bas à droite
        i = x-1
        j = y+1        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[1] += 1
            i -= 1
            j += 1
            
        if (tableau[1] >= Puissance4.n):
            #print("le joueur {} a gagné".format(joueur))
           return True
        
        #Vers la droite
        i = x
        j = y        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[2] += 1
            j += 1
        #Vers la gauche
        i = x
        j = y-1        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[2] += 1
            j -= 1
        
        if (tableau[2] >= Puissance4.n):
            #print("le joueur {} a gagné".format(joueur))
           return True          
        #Vers le bas à gauche
        i = x
        j = y        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[3] += 1
            i -= 1            
            j -= 1
        #Vers le haut à droite
        i = x+1
        j = y+1        
        while (0 <= i < Puissance4.hauteur) and (0 <= j < Puissance4.longueur) and (matrice_test[i,j] == 1):
            tableau[3] += 1
            i += 1
            j += 1
        
        if (tableau[3] >= Puissance4.n):
            #print("le joueur {} a gagné".format(joueur))
            return True
        
        #print tableau
        return False
       

    def afficher(self):
        self.canvas.delete("J1")
        self.canvas.delete("J2")
        for i in xrange(Puissance4.hauteur):
            for j in xrange(Puissance4.longueur):
                if (self.matrice_J1[i,j] == 1):
                    x0, y0 = convert_coordinates(i, j+1)
                    x1, y1= convert_coordinates(i+1, j)
                    self.canvas.create_oval(y0, Puissance4.H-x0, y1, Puissance4.H-x1, outline="gray", fill="red", width=2, tag="J1")
                if (self.matrice_J2[i,j] == 1):
                    x0, y0 = convert_coordinates(i, j+1)
                    x1, y1= convert_coordinates(i+1, j)
                    self.canvas.create_oval(y0, Puissance4.H-x0, y1, Puissance4.H-x1, outline="gray", fill="yellow", width=2, tag="J2")
        self.frame.update()

    def coups_possibles(self):
        l = []
        for i,elt in enumerate(self.tableau_jeu):
            if (elt < Puissance4.hauteur-1):
                l.append(i)
        return l

            
    def retirer(self,colonne):
        s = self.tableau_jeu[colonne]
        self.tableau_jeu[colonne] -= 1
        if (self.matrice_J1[s-1,colonne] == 1):
            self.matrice_J1[s-1,colonne] = 0
        if (self.matrice_J2[s-1,colonne] == 1):
            self.matrice_J2[s-1,colonne] = 0


    def partie_IA(self):
#        self.reset()
#        self.frame.bind("<Button-1>", self.callback)
#        self.frame.pack()
        ARTIF = IA.P4IA(self, 2)
        coup = ARTIF.coup_IA()
        print coup
        self.jouer(coup, 2)

#a = Puissance4()
#joueur = 1
#a.mainloop()






        