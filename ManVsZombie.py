# -*- coding : utf-8 -*-
import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode(resolution)

#Icone
pygame.display.set_icon(img_zd1)

#Titre
pygame.display.set_caption(titre_fenetre)

#Boucle
continuer = 1
menu = 1
jeu = 1
fin = 0 
i = 0

#Horloge qui permet de mesurer le temps
clock = pygame.time.Clock()

#Permet de répéter l'action si la touche reste pressée
pygame.key.set_repeat(50, 110)

# Variables et rect nécessairenments définie ici
list_bullet = []
solr = Rect((-100, hauteur_ecran - 136), (10000,150))
pla2 = Rect((500, hauteur_pla), (458, 60))
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
                if event.key == K_F1: #Si l'utilisateur choisi de lancer le je
                    menu = 0
                    jeu = 1
                    zk = 0
                    # On crée tout les objets du niveau 
                    z1 = Zombie(fenetre, 800)
                    z2 = Zombie(fenetre, 900, hauteur_pla-150)
                    z3 = Zombie(fenetre, 900, 1000)
                    z4 = Zombie(fenetre, 900, 1000)
                    z5 = Zombie(fenetre, 900, 1000)
                    niv = Niveau(fenetre) 
                    perso = Perso(fenetre, niv, [pla2, solr,z1.rect ,z2.rect], [z1, z2, z3, z4, z5])#On indique en paramètre a notre perso une liste de tout les rects afin de gérer les collisions
                    fenetre.blit(img_cr, (300, 372))
                    niv.create(perso, z1, z2, z3, z4, z5)
                    pygame.display.flip()

                if event.key == K_F2:
                	continuer = 0
                	menu = 0
                	jeu = 0

    while jeu == 1: #Boucle de jeu
        if perso.isdead([z1.rect, z2.rect]) == True:
            jeu = 0
            menu = 1
            img_acceuil = img_mort
        pygame.time.Clock().tick(60) #On limite la boucle a 60 répétition par secondes
        z1.moove(perso)
        z2.moove(perso)
        z3.moove(perso)
        z4.moove(perso)
        z5.moove(perso)
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
        """Ici on actualise tout les éléments présents a l'écran pour chaque Frame"""
        niv.create(perso, z1, z2, z3, z4, z5)
        #On regarde si le joueur a tué les deux premiers zombies et si il a tué tout les autres zombies
        nivstate(zk, z1, z2, z3, z4, z5, perso)
        if nivstate(zk, z1, z2, z3, z4, z5, perso) == True:
            jeu = 0
            fin = 1
        
        #Les encapsulation sont ici afin d'éviter les erreurs dues a la non existence des balles si elles n'ont pas encore étées tirées
        try :
            list_bullet.remove(b0)
            b0.moove()
            fenetre.blit(b0.img, (b0.x, b0.y))
            list_bullet.append(b0)
        except:
            a = 1
        try :
            list_bullet.remove(b1)
            b1.moove()
            fenetre.blit(b1.img, (b1.x, b1.y))
            list_bullet.append(b1)
        except:
            a = 1
        try :
            list_bullet.remove(b2)
            b2.moove()
            fenetre.blit(b2.img, (b2.x, b2.y))
            list_bullet.append(b2)
        except:
            a = 1
        try :
            list_bullet.remove(b3)
            b3.moove()
            fenetre.blit(b3.img, (b3.x, b3.y))
            list_bullet.append(b3)
        except:
            a = 1
        try :
            list_bullet.remove(b4)
            b4.moove()
            fenetre.blit(b4.img, (b4.x, b4.y))
            list_bullet.append(b4)
        except:
            a = 1
        #tout ce aui doit etre répété constament afin d'afficher le niveau et l'ensemble
        perso.collide(perso.List_collide)
        if z1.collide(list_bullet) == True:
            z1.disapear()
            zk += 1
        if z2.collide(list_bullet) == True:
            z2.disapear()
            zk += 1
        if z3.collide(list_bullet) == True:
            z3.disapear()
            zk += 1
        if z4.collide(list_bullet) == True:
            z4.disapear()
            zk += 1
        if z5.collide(list_bullet) == True:
            z5.disapear()
            zk += 1
        fenetre.blit(perso.img,(perso.x, perso.y))
        fenetre.blit(z1.img, (z1.x, z1.y) )
        fenetre.blit(z2.img, (z2.x, z2.y) )
        fenetre.blit(z3.img, (z3.x, z3.y) )
        fenetre.blit(z4.img, (z4.x, z4.y) )
        fenetre.blit(z4.img, (z4.x, z4.y) )
        fenetre.blit(z5.img, (z5.x, z5.y) )
        pygame.display.flip()

    while fin == 1:
        fenetre.blit(img_fin, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_F1:
                fin = 0
                continuer = 0
