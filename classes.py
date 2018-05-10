import pygame
from constantes import *
from pygame.locals import *
from math import *

class Niveau():
    def __init__(self, Fenetre):
        """Constructeur de notre classe Niveau on y dÃ©fini toute les variables
        Communes a tout les objets Niveau"""
        self.fen = Fenetre
        self.fond = img_fond
        self.sol = img_sol
        scrolling_x = 0

    def create(self, perso,z1, z2):
        """On va ici crÃ©er tout ce qui est nÃ©cessaire afin que notre fonction
        Afficher_niveau puisse afficher le niveau, cela permet de rÃ©afficher le
        niveau sans recalculer la position des objets sauf si nÃ©cessaire"""
        z1.moove(perso.x)
        z2.moove(perso.x)
        self.fen.blit(self.fond, (0, 0))
        self.fen.blit(self.fond, (1280, 0))
        self.fen.blit(self.sol, (0, hauteur_ecran-136))
        self.fen.blit(self.sol, (801, hauteur_ecran-136))
        self.fen.blit(img_pla2, (500, 380))
        self.fen.blit(z1.img, (z1.x, z1.y))
        self.fen.blit(z2.img, (z2.x, z2.y))


class Perso():
    def __init__(self, Fenetre, niveau, list, ennemi_list):
        """Constructeur de notre classe Niveau on y défini toute les variables
        Communes a tout les objets Perso"""
        self.i = 0
        self.fen = Fenetre
        self.niv = niveau
        self.x = 0
        self.y = 372  #Niveau du sol
        #Nous créons ici des listes afin d'uiliser plus facilement les sprite (for)
        self.D = [img_d1, img_d2, img_d3, img_d4, img_d5, img_d6]
        self.G = [img_g1, img_g2, img_g3, img_g4, img_g5, img_g6]
        self.SD = [img_sd1, img_sd2, img_sd3, img_sd4, img_sd5]
        self.SG = [img_sg1, img_sg2, img_sg3, img_sg4, img_sg5]
        self.img =  img_d1  #Image utilisée actuellement
        self.rect = Rect((self.x, self.y), (100,137))
        self.List_collide = list
        self.ennemis = ennemi_list

    def jump(self, direction):
        """Gère le saut"""
        k = 10
        y = self.y - 172
        if direction == "droite":
            while self.y > y:
                self.collide(self.List_collide)
                pygame.time.Clock().tick(30)
                self.y -= 10
                self.x += 8
                print(self.x)
                print(self.y)
                self.niv.create(self, self.ennemis[0], self.ennemis[1])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k -= 0.3
            while self.collide(self.List_collide) == False:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y += 10
                self.x += 8
                print(self.x)
                print(self.y)
                self.niv.create(self, self.ennemis[0], self.ennemis[1])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k += 0.3

        if direction == "verticale":
            while self.y > y:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y -= 10
                print(self.x)
                print(self.y)
                self.niv.create(self, self.ennemis[0], self.ennemis[1])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()

            while self.collide(self.List_collide) == False:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y += 10
                print(self.x)
                print(self.y)
                self.niv.create(self, self.ennemis[0], self.ennemis[1])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()

        if direction == "gauche":
            while self.y > y:
                self.collide(self.List_collide)
                pygame.time.Clock().tick(30)
                self.y -= 10
                self.x -= 8
                print(self.x)
                print(self.y)
                self.niv.create(self, self.ennemis[0], self.ennemis[1])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k -= 0.3
            while self.collide(self.List_collide) == False:
                pygame.time.Clock().tick(30)
                self.collide(self.List_collide)
                self.y += 10
                self.x -= 8
                print(self.x)
                print(self.y)
                self.niv.create(self, self.ennemis[0], self.ennemis[1])
                self.fen.blit(self.img,(self.x, self.y))
                pygame.display.flip()
                k += 0.3


    def moove(self, direction):
        """Permet de déplacer le personnage"""
        if direction == "droite":
            if self.x >= largeur_ecran - 137:
                return 0
            if self.i < 5 :
                self.i += 1
            else :
                self.i = 0
            if self.i == 3:
                self.x += 10
            self.img = self.D[self.i]
            self.x += 20

        if direction == "gauche":
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
        """Vérifie certain paramètre lors d'une collision"""
        self.rect = Rect((self.x, self.y), (100,137))
        if self.rect.collidelist(list) == 0:
            print("collide zombie")
        if self.rect.collidelist(list) == 1 or self.rect.collidelist(list) == 2:
            return True
        elif self.rect.collidelist(list) == 1 and self.rect.collidelist(list) == 2:
            return True
        else:
            return False

class Zombie():
    def __init__(self, Fenetre, x, y = 372):
        """Constructeur de notre classe Niveau on y défini toute les variables
        Communes a tout les objets Perso"""
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
        self.rect = Rect((self.x, self.y), (100,137))


    def user_near(self, user_x):
        """Retourne un booléen qui dépend de la distance entre le joueur et le zombie"""
        if user_x < self.x and self.x - user_x < 200:
            return True

        elif user_x - self.x < 200:
            return True

        else :
            return False

    def moove(self, user_x):
        """Gère les mouvements du zombie"""
        if self.user_near(user_x) == True:
            self.i = 0

            if user_x > self.x:
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

    def collide(self, list):
        """Vérifie certain paramètre lors d'une collision"""
        self.rect = Rect((self.x, self.y), (100,137))
        if self.rect.collidelist(list) != -1:
            print("zombie hit by bullet")
            return True

    def disapear(self):
        self.y = 5000

class Bullet():
    def __init__(self, perso, direction):
        self.direction = direction
        if direction == "droite":
            self.x = perso.x + 100
        else:
            self.x = perso.x
        self.y = perso.y + 38
        self.img = img_bullet
        self.rect = Rect((self.x, self.y), (10,5))

    def moove(self):
        if self.direction == "droite":
            self.x += 5
        else:
            self.x -= 5
        self.rect = Rect((self.x, self.y), (10,5))
