# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:27:56 2016

@author: thomas
"""

# IA du Puissance4

import Puissance4.py

# Pour les 7 coups possibles j'obtient la note récursivement

class P4IA:
    
    
    
    def jouerIA(self,p,joueur):
        for i in range(Puissance4.longueur):
            if p.jouer(i,joueur):
                return i
            p.retirer(i,joueur)
            
            