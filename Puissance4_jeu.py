# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:30:17 2016

@author: Maxime
"""

import numpy as np
import random as rd
from Tkinter import *

def convert_coordinates(i, j):#Converti les coordonnées dans le tableau en coordonnée sur la fenêtre
    return Puissance4.H - (Puissance4.hauteur-i) * Puissance4.H / Puissance4.hauteur, j * Puissance4.L / Puissance4.longueur

class Puissance4(Tk):
    
    L = 500 #Largeur de la fenêtre
    longueur = 7
    hauteur = 6
    H = hauteur*1./longueur * L
    n = 4
    
    
    def __init__(self):
        Tk.__init__(self)
        self.matrice_J1 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.matrice_J2 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.tableau_jeu = np.zeros(Puissance4.longueur)
        self.frame = Frame(self, width=Puissance4.L, height=Puissance4.H)
        self.canvas = Canvas(self, width=Puissance4.L, height=Puissance4.H, bg="white")
        self.canvas.pack()
    
    def reset(self):
        self.matrice_J1 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.matrice_J2 = np.zeros((Puissance4.hauteur,Puissance4.longueur))
        self.tableau_jeu = np.zeros(Puissance4.longueur)
        self.frame = Frame(self, width=Puissance4.L, height=Puissance4.H)
        self.canvas = Canvas(self, width=Puissance4.L, height=Puissance4.H, bg="white")
        self.canvas.pack()


    
    def jouer(self,poz,joueur):
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
            if self.coup_gagnant(high, poz,joueur):
                self.reset()
                return
            self.tableau_jeu[poz] = high+1
            self.afficher()
            
        #print self.matrice_J1

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
            print("le joueur {} a gagné".format(joueur))
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
            j =+ 1
            
        if (tableau[1] >= Puissance4.n):
           print("le joueur {} a gagné".format(joueur))
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
           print("le joueur {} a gagné".format(joueur))
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
            print("le joueur {} a gagné".format(joueur))
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
        self.canvas.update()
        self.canvas.update()


    def coup_au_hasard(self, joueur):
        r = rd.randint(0,Puissance4.longueur-1)
        print r
        try:
            self.jouer(r, joueur)
        except ValueError:
            coup_au_hasard(self, joueur)
        except IndexError:
            self.reset()

a = Puissance4()
s = 0
while True:
    print s
    r = rd.randint(0,Puissance4.longueur-1)
    a.jouer(r, s%2+1)
    a.afficher()
    a.after(500)
    s+=1





        