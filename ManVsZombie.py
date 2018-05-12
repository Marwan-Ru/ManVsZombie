# -*- coding : utf-8 -*-
import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

#Ouverture de la fenÃ¨tre Pygame
fenetre = pygame.display.set_mode(resolution)

#Icone
pygame.display.set_icon(img_zd1)

#Titre
pygame.display.set_caption(titre_fenetre)

#Boucle
continuer = 1
menu = 1
jeu = 1
i = 0

#Horloge qui permet de mesurer le temps
clock = pygame.time.Clock()

#Permet de répéter l'action si la touche reste pressée
pygame.key.set_repeat(50, 110)

# Variables et rect nécessairenments définie ici
list_bullet = []
solr = Rect((-100, hauteur_ecran - 136), (10000,150))
pla2 = Rect((500, 380), (458, 60))
direction = "immobile"

while continuer == 1:
    clock.tick(30)# on limite la boucle a 30 fps
    while menu == 1:
        #Affichage du menu
        fenetre.blit(img_accueil, (0,0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT: # Si on appuie sur la croix rouge
                jeu = 0
                menu = 0
                continuer = 0
                pygame.display.quit()
            if event.type == KEYDOWN:
                if event.key == K_F1: #Si l'utilisateur choisi de lancer le jeu
                    menu = 0
                    jeu = 1
                    print("JEU")
                    # On crée tout les objets du niveau 
                    niv = Niveau(fenetre) 
                    z1 = Zombie(fenetre, 800)
                    z2 = Zombie(fenetre, 900, 245)
                    perso = Perso(fenetre, niv, [z1.rect, pla2, solr, z2.rect], [z1, z2])#On indique en paramètre a notre perso une liste de tout les rects afin de gérer les collisions
                    fenetre.blit(img_cr, (300, 372))
                    niv.create(perso, z1, z2)
                    pygame.display.flip()

                if event.key == K_F2:
                	continuer = 0
                	menu = 0
                	jeu = 0

    while jeu == 1: #Boucle de jeu
        pygame.time.Clock().tick(60) #On limite la boucle a 60 répétition par secondes
        z1.moove(perso)
        z2.moove(perso)
        for event in pygame.event.get():
            if event.type == QUIT: #Si on appuie sur la croix on ferme la fenètre et le programme
                jeu = 0
                menu = 0
                continuer = 0
                pygame.display.quit()
            if event.type == KEYDOWN: #Si l'on appuie sur une touche
                if event.key == K_d: #Et que cette touche est la touche D
                    perso.moove("droite") #Alors on déplace le personnage vers la droite
                    direction = "droite"
                if event.key == K_a: #Idem avec q
                    perso.moove("gauche")
                    direction = "gauche"
                if event.key == K_s:
                    direction = "immobile"
                if event.key == K_w and direction == "droite": #Idem
                    print("DZAGHYDIAZGGZAYIDGAZI")
                    perso.jump("droite")
                if event.key == K_w and direction == "gauche": #Idem
                    perso.jump("gauche")
                elif event.key == K_w and direction == "immobile":
                    perso.jump("verticale")
                if event.key == K_RIGHT:  #On regarde le coté du tir et on limite le nombre de balle a 5
                    print("droite")
                    if i == 0:
                        b0 = Bullet(perso, "droite")
                        list_bullet.append(b0.rect)
                    elif i == 1:
                        b1 = Bullet(perso, "droite")
                        list_bullet.append(b1.rect)
                    elif i == 2:
                        b2 = Bullet(perso, "droite")
                        list_bullet.append(b2.rect)
                    elif i == 3:
                        b3 = Bullet(perso, "droite")
                        list_bullet.append(b3.rect)
                    elif i == 4:
                        b4 = Bullet(perso, "droite")
                        list_bullet.append(b4.rect)
                    else:
                        print("i max atteint")
                    i += 1
                if event.key == K_LEFT:
                    print("gauche")
                    if i == 0:
                        b0 = Bullet(perso, "gauche")
                        list_bullet.append(b0.rect)
                    elif i == 1:
                        b1 = Bullet(perso, "gauche")
                        list_bullet.append(b1.rect)
                    elif i == 2:
                        b2 = Bullet(perso, "gauche")
                        list_bullet.append(b2.rect)
                    elif i == 3:
                        b3 = Bullet(perso, "gauche")
                        list_bullet.append(b3.rect)
                    elif i == 4:
                        b4 = Bullet(perso, "gauche")
                        list_bullet.append(b4.rect)
                    else:
                        print("i max atteint")
                    i += 1
                if event.key == K_r and i > 5: #Si toute les balles on étées tirée le joueur peut recharger avec la touche r
                    i = 0
                    list_bullet.clear()
                    del b0, b1, b2, b3, b4
                print("self.x = " + str(perso.x) + " self.y = " + str(perso.y))#Ce print est présent uniquement afin de vérifier la position du personnage dans la console
                print(str(perso.rect) + " précedent") #Et celui la pour vérifier que le rect est bien sur le personnage
        """Ici on actualise tout les éléments présents a l'écran pour chaque Frame"""
        niv.create(perso, z1, z2)
        #Les encapsulation sont la afin d'éviter les erreurs dues a la non existence des balles si elles n'ont pas encore étées tirées
        try :
            list_bullet.remove(b0)
            b0.moove()
            fenetre.blit(b0.img, (b0.x, b0.y))
            list_bullet.append(b0)
        except:
            print("Pas de b0")
        try :
            list_bullet.remove(b1)
            b1.moove()
            fenetre.blit(b1.img, (b1.x, b1.y))
            list_bullet.append(b1)
        except:
            print("Pas de b1")
        try :
            list_bullet.remove(b2)
            b2.moove()
            fenetre.blit(b2.img, (b2.x, b2.y))
            list_bullet.append(b2)
        except:
            print("Pas de b2")
        try :
            list_bullet.remove(b3)
            b3.moove()
            fenetre.blit(b3.img, (b3.x, b3.y))
            list_bullet.append(b3)
        except:
            print("Pas de b3")
        try :
            list_bullet.remove(b4)
            b4.moove()
            fenetre.blit(b4.img, (b4.x, b4.y))
            list_bullet.append(b4)
        except:
            print("Pas de b4")
        #tout ce aui doit etre répété constament afin d'afficher le niveau et l'ensemble
        perso.collide(perso.List_collide)
        if z1.collide(list_bullet) == True:
            z1.disapear()
        if z2.collide(list_bullet) == True:
             z2.disapear()
        fenetre.blit(perso.img,(perso.x, perso.y))
        fenetre.blit(z1.img, (z1.x, z1.y) )
        fenetre.blit(z2.img, (z2.x, z2.y) )
        pygame.display.flip()
