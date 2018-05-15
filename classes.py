# -*- coding: utf-8 -*-
import pygame
from constantes import *
from pygame.locals import *
from math import *

class Niveau():
    def __init__(self, Fenetre):
        """Constructeur de notre classe Niveau on y dÃ©fini toute les variables
        Communes a tout les objets Niveau"""
        # :parametre fenetre [Fenetre ou le niveau s'affiche]
        self.fen = Fenetre

    def create(self, perso, z1, z2, z3, z4, z5):
        """Cette méthode permet de raffraichir le niveau cylcliquement et permet d'éviter ainsi les répétition dans le code de ManVsZombie"""
        z1.moove(perso)
        z2.moove(perso)
        self.fen.blit(img_fond, (0, 0))
        self.fen.blit(img_fond, (1280, 0))
        self.fen.blit(img_sol, (0, hauteur_ecran-136))
        self.fen.blit(img_sol, (801, hauteur_ecran-136))
        self.fen.blit(img_pla2, (500, hauteur_pla))
        self.fen.blit(z1.img, (z1.x, z1.y))
        self.fen.blit(z2.img, (z2.x, z2.y))
        self.fen.blit(z3.img, (z3.x, z3.y))
        self.fen.blit(z4.img, (z4.x, z4.y))
        self.fen.blit(z5.img, (z5.x, z5.y))


class Perso():
    def __init__(self, Fenetre, niveau, list, ennemi_list):
        """Constructeur de notre classe Perso on y défini toute les variables
        Communes a tout les objets Perso"""
        # :parametre Fenetre [Fenetre ou le niveau va s'afficher]
        # :parametre niveau [Objet niveau affili� au perso]
        # :parametre list [Liste des rects avecs lequels le Perso doit r�agir en collision]
        # :parametre ennemi_list [Liste des objets consid�r�s comme ennemis]
        self.i = 0
        self.fen = Fenetre
        self.niv = niveau
        self.x = 0
        self.y = 349  #Niveau du sol
        #Nous créons ici des listes afin d'uiliser plus facilement les sprite (for)
        self.D = [img_d1, img_d2, img_d3, img_d4, img_d5, img_d6]
        self.G = [img_g1, img_g2, img_g3, img_g4, img_g5, img_g6]
        self.img =  img_d1  #Image utilisée actuellement
        self.rect = Rect((self.x, self.y), (100,160))
        self.List_collide = list
        self.ennemis = ennemi_list

    def jump(self, direction):
        # :parametre direction [Direction dans laquelle le personnage se dirige actuellement]
        """Méthode qui gère le saut"""
        k = 10
        y = self.y - 172 #Permet d'adapter la hauteur du saut en fonction du la hauteur ou notre personnage se trouve
        if direction == "droite":
            while self.y > y:
                self.collide(self.List_collide)#On lance la méthode qui permet de gérer les collisions
                pygame.time.Clock().tick(30)#On limite les fps a 30
                self.y -= 10
                self.x += 8
                self.niv.create(self, self.ennemis[0], self.ennemis[1], self.ennemis[2], self.ennemis[3], self.ennemis[4])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k += 0.3

            while self.collide(self.List_collide) == False:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)#On lance la méthode qui permet de gérer les collisions
                self.y += 10
                self.x += 8
                self.niv.create(self, self.ennemis[0], self.ennemis[1], self.ennemis[2], self.ennemis[3], self.ennemis[4])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                

        if direction == "verticale":
            while self.y > y:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y -= 10
                #Ici on effectue un saut a la verticale le x n'est donc pas modifié
                self.niv.create(self, self.ennemis[0], self.ennemis[1], self.ennemis[2], self.ennemis[3], self.ennemis[4])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()

            while self.collide(self.List_collide) == False:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y += 10
                self.niv.create(self, self.ennemis[0], self.ennemis[1], self.ennemis[2], self.ennemis[3], self.ennemis[4])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()

        if direction == "gauche":
            while self.y > y:
                self.collide(self.List_collide)
                pygame.time.Clock().tick(30)
                self.y -= 10
                self.x -= 8
                self.niv.create(self, self.ennemis[0], self.ennemis[1], self.ennemis[2], self.ennemis[3], self.ennemis[4])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k -= 0.3
            while self.collide(self.List_collide) == False:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y += 10
                self.x -= 8
                self.niv.create(self, self.ennemis[0], self.ennemis[1], self.ennemis[2], self.ennemis[3], self.ennemis[4])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k += 0.3


    def moove(self, direction):
        """Permet de déplacer le personnage on inclue en parametre la direction afin de n'avoir qu'une seule méthode a appeler pour toutes les directions"""
        # :parametre direction [Direction dans laquelle doit se diriger le personnage]
        if direction == "droite": #Si le personnage doit se d
            if self.x >= largeur_ecran - 137: #Si le personnage sors de l'écran par la droite (Sa largeur est de 137px)
                self.x = largeur_ecran - 137
            if self.i < 5 : #On vérifie aue l'on ne sort pas de limites de la liste de sprites
                self.i += 1
            else : #Si jamais om en sors on revien au debut
                self.i = 0
            if self.i == 3: #lors du sprite a l'index 3 de la liste le personnage fait un pas différent son déplacement est donc ajusté
                self.x += 10
            self.img = self.D[self.i]#On prend un sprite dans la liste de sprite le i permet de parcourir la liste sans stoper l'action du jeu avec une boucle for
            self.x += 20

        if direction == "gauche": #Idem mais vers la gauche
            if self.x <=0:
                return 0
            if self.i < 5 :
                self.i += 1
            else :
                self.i = 0
            if self.i == 3:
                self.x -= 10
            self.img = self.G[self.i]
            self.x -= 20

    def collide(self, list):
        """Permet de savoir quelle type de collision a eu lieu si jamais collision il y a"""
        self.rect = Rect((self.x, self.y), (100,160))
        if self.rect.collidelist(list) <= 1 and self.rect.collidelist(list) != -1:#Si la collision a lieu avec une plateforme
            return True
        else: #Sinon cela veut dire qu'aucune collision n'a eu lieu
            return False

    def isdead(self, list):
        self.rect = Rect((self.x, self.y), (100,160))
        if self.rect.collidelist(list) != -1: #si la collision a lieu avec un zombie
            return True
        else:
            return False

class Zombie():
    """Classe créée pour les zombie elle gère :
        - Les déplacement du zombie qui sont différents selon sa proximité avec le joueur
        - Les collisions du zombie avec son environnement
        """
    def __init__(self, Fenetre, x, y = 367):
        """Constructeur de notre classe Zombie on y défini toute les variables
        Communes a tout les objets Zombie"""
        # parametre Fenetre [Fenetre a laquelle le zombie est affili�]
        # parametre x [Position x de d�part]
        # parametre y [Position y de d�part avec une valeur par d�faut de  367]
        self.i = 0
        self.fen = Fenetre
        self.x = x
        self.y = y   #Niveau du sol
        #Nous créons ici des listes afin d'uiliser plus facilement les sprite
        self.ZD = [img_zd1, img_zd2, img_zd3, img_zd4]
        self.ZG = [img_zg1, img_zg2, img_zg3, img_zg4]
        self.MZD =[img_mzd1, img_mzd2, img_mzd3]
        self.MZG =[img_mzg1, img_mzg2, img_mzg3]
        self.img =  img_zd1  #Image utilisée actuellement
        self.rect = Rect((self.x, self.y), (74,150))
        self.p = 0

    def user_near(self, user_x):
        """Retourne un booléen qui dépend de la distance entre le joueur et le zombie"""
        # parametre user_x [Position du perso sur l'axe des abscisse]
        if user_x < self.x and self.x - user_x < 200:
            return True

        elif user_x - self.x < 200:
            return True

        else :
            return False

    def moove(self, perso):
        """Gère les mouvements du zombie selon le booléen retourné par user_near()"""
        #parametre perso [Objet Perso() repr�sentant le joueur]
        if self.y == 367 :
            if self.user_near(perso.x) == True:
                self.i = 0

                if perso.x > self.x: # Si l'utilisateur est plus loin sur l'axe des abscisse que le l'objet zombie
                    self.x += 2
                else:
                    self.x -= 2

            else:
                self.i += 1
                if self.i <= 200:
                    self.x += 1
                elif self.i <= 400 and self.i > 200:
                    self.x -= 1
                else:
                    self.i = 0
        else:
            self.on_platform(perso)
    
    def collide(self, list):
        """Vérifie certain paramètre lors d'une collision"""
        self.rect = Rect((self.x, self.y), (100,137))
        if self.rect.collidelist(list) != -1:
            print("zombie hit by bullet")
            return True

    def disapear(self):
        self.y = 5000
    
    def on_platform(self, perso):
        if self.x > 799:
            self.p = 0
        if self.x < 501:
            self.p = 1
        if self.x > 500 and self.p == 0: #Si l'on n'a pas attein le cot� gauche de la plateforme et que le c�t� droit a �t� attein pr�c�dement
            self.x -= 1
        if self.x < 800 and self.p == 1:
            self.x += 1

class Bullet():
    """Classe des balles tirée par le soldat elle gère:
        - Le mouvement de la balle et de son rect associé
        - A terme la disparition de la balle lorsqu'elle touche un zomnie (A voir)
        """
    def __init__(self, perso, direction):
        """Constructeur de la classe Bullet qui définis le s variables communes a tout les objets bullet"""
        # :parametre perso [Objet perso repr�sentant le joueur]
        # :parametre direction [Direction initiale de la balle (ne peut pes changer)]
        self.direction = direction
        if direction == "droite": #Si la balle est tirée vers la droite
            self.x = perso.x + 100 #Elle partira de la droite du personnage (La largeur du perso est de 100px)
        else:
            self.x = perso.x #Sinon elle pars de la gauche du perso
        self.y = perso.y + 38 #Position du cannon du fusil du soldat en fonction de sa position
        self.img = img_bullet
        self.rect = Rect((self.x, self.y), (10,5))
        self.list = perso.List_collide

    def moove(self):
        self.rect = Rect((self.x, self.y), (10,5))
        if self.direction == "droite":
            self.x += 5
        else:
            self.x -= 5

def nivstate(zk, z1, z2, z3, z4, z5):
    try:
        print(niv1 + niv2 + niv3)
    except:
        niv1 = "lance"
        niv2 = "lance"
        niv3 = "lance"

    if zk == 2 and niv1 == "lance":
        niv1 = "fini"
        zk = 0
    if zk == 3 and niv2 == "lance":
        niv2 == "fini"
        zk = 0
    if niv2 == "fini" and niv3 == "lance":
        niv3 == "fini"
        zk = 0

    if niv1 == "fini":
        z1.y, z1.x= 367, 900
        z2.y, z2.x = 367, 600
        z3.y, z3.x = hauteur_pla-150, 900
        niv1 == "Supprime"
    if niv2 == "fini":
        z1.y, z1.x= 367, 900
        z2.y, z2.x = 367, 600
        z3.y, z3.x = hauteur_pla-150, 900
        z4.y, z4.x = 367, 100
        z5.y, z5.x = hauteur_pla-150, 900
        niv2 == "supprime"
    if niv3 == "fini":
        Fin = 1
        jeu = 0
        menu = 1
    
