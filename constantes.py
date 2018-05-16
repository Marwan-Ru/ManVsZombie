# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

fen = pygame.display.set_mode((1,1))
"""Constantes utilisées par notre jeu
rassemblée ici afin de faciliter la modification de celles ci"""

"""Sprites de  marche du soldat"""

#Vers la droite
img_d1 = pygame.image.load("Img/D/d1.png").convert_alpha()
img_d2 = pygame.image.load("Img/D/d2.png").convert_alpha()
img_d3 = pygame.image.load("Img/D/d3.png").convert_alpha()
img_d4 = pygame.image.load("Img/D/d4.png").convert_alpha()
img_d5 = pygame.image.load("Img/D/d5.png").convert_alpha()
img_d6 = pygame.image.load("Img/D/d6.png").convert_alpha()

#Vers la gauche
img_g1 = pygame.image.load("Img/G/g1.png").convert_alpha()
img_g2 = pygame.image.load("Img/G/g2.png").convert_alpha()
img_g3 = pygame.image.load("Img/G/g3.png").convert_alpha()
img_g4 = pygame.image.load("Img/G/g4.png").convert_alpha()
img_g5 = pygame.image.load("Img/G/g5.png").convert_alpha()
img_g6 = pygame.image.load("Img/G/g6.png").convert_alpha()

"""Sprites de saut du soldat"""

#Vers la droite
img_sd1 = pygame.image.load("Img/SD/sd1.png").convert_alpha()
img_sd2 = pygame.image.load("Img/SD/sd2.png").convert_alpha()
img_sd3 = pygame.image.load("Img/SD/sd3.png").convert_alpha()
img_sd4 = pygame.image.load("Img/SD/sd4.png").convert_alpha()
img_sd5 = pygame.image.load("Img/SD/sd5.png").convert_alpha()

#Vers la gauche
img_sg1 = pygame.image.load("Img/SG/sg1.png").convert_alpha()
img_sg2 = pygame.image.load("Img/SG/sg2.png").convert_alpha()
img_sg3 = pygame.image.load("Img/SG/sg3.png").convert_alpha()
img_sg4 = pygame.image.load("Img/SG/sg4.png").convert_alpha()
img_sg5 = pygame.image.load("Img/SG/sg5.png").convert_alpha()

"""Sprites de marche du zombie"""

#Vers la droite
img_zd1 = pygame.image.load("Img/ZD/zd1.png").convert_alpha()
img_zd2 = pygame.image.load("Img/ZD/zd2.png").convert_alpha()
img_zd3 = pygame.image.load("Img/ZD/zd3.png").convert_alpha()
img_zd4 = pygame.image.load("Img/ZD/zd4.png").convert_alpha()

#Vers la gauche
img_zg1 = pygame.image.load("Img/ZG/zg1.png").convert_alpha()
img_zg2 = pygame.image.load("Img/ZG/zg2.png").convert_alpha()
img_zg3 = pygame.image.load("Img/ZG/zg3.png").convert_alpha()
img_zg4 = pygame.image.load("Img/ZG/zg4.png").convert_alpha()

"""Sprites de mort du zombie"""

#Vers la droite
img_mzd1 = pygame.image.load("Img/MZD/mzd1.png").convert_alpha()
img_mzd2 = pygame.image.load("Img/MZD/mzd2.png").convert_alpha()
img_mzd3 = pygame.image.load("Img/MZD/mzd3.png").convert_alpha()

#Vers la gauche
img_mzg1 = pygame.image.load("Img/MZG/mzg1.png").convert_alpha()
img_mzg2 = pygame.image.load("Img/MZG/mzg2.png").convert_alpha()
img_mzg3 = pygame.image.load("Img/MZG/mzg3.png").convert_alpha()

"""Sprites de test"""
#Carré rouge et carré bleu
img_cr = pygame.image.load("Img/cr.png").convert_alpha()
img_cb = pygame.image.load("Img/cb.png").convert_alpha()
img_bullet = pygame.image.load("Img/F/bullet.png").convert_alpha()

"""Sprites de fond et de plateforme"""
#Fond du jeu et sol
img_accueil = pygame.image.load("Img/F/accueil.png").convert_alpha()
img_mort = pygame.image.load("Img/F/mort.jpg")
img_fin = pygame.image.load("Img/F/gagne.jpg")
img_fond = pygame.image.load("Img/F/fond.png").convert_alpha()
img_sol = pygame.image.load("Img/F/sol.jpg").convert()

#Plateformes
img_pla1 = pygame.image.load("Img/F/pla1.png").convert_alpha()
img_pla2 = pygame.image.load("Img/F/pla2.png").convert_alpha()
img_pla3 = pygame.image.load("Img/F/pla3.png").convert_alpha()
img_pla4 = pygame.image.load("Img/F/pla4.png").convert_alpha()

"""Différent rects nécessaires aux collisions"""
rect2 = Rect(300, 372,100 ,140)
rects_ennemis = [rect2]

"""Constantes numérique"""
largeur_sprite = 100
hauteur_sprite = 140
largeur_ecran = 1280
hauteur_ecran = 645
largeur_niveau = 2560
hauteur_pla = 360 
resolution = (largeur_ecran, hauteur_ecran)
titre_fenetre = "ManVsZombie"
