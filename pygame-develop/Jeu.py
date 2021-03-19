import pygame
import sys
import random
import math
import socket
import threading
from game import Game
from Client import Client

class Jeu:

    def __init__(self):
        # init Client
        self.client = Client("marco", "localhost", 59001)
        self.client.listen()
        self.client2 = Client("MARCO BIS", "localhost", 59001)
        self.client2.listen()

        # définir une clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # générer la fenetre du jeu
        pygame.display.set_caption("World War Worms")
        self.screen = pygame.display.set_mode((1080, 720))

        # Charger l'arrière plan
        self.background = pygame.image.load('assets/background.jpg')

        # importer charger notre bannière
        self.banner = pygame.image.load('assets/banner.png')
        self.banner = pygame.transform.scale(self.banner, (500, 500))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width() / 4)

        # importer charger notre bouton pour lancer la partie
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)

        self.game = Game(self.client, self.client2)



    def boucle_principale(self):
        running = True
        while running:
            # tant que le jeu est actif

            # arrière plan
            self.screen.blit(self.background, (0, 0))

            # verifier si notre jeu a commencé
            if self.game.is_playing:
                # declencher les instructions de la partie
                self.game.update(self.screen)
            else:
                # ajouté mon écran de bienvenue
                self.screen.blit(self.play_button, self.play_button_rect)
                self.screen.blit(self.banner, self.banner_rect)

            # mettre à jour l'ecran
            pygame.display.flip()

            # si le joueur ferme la fenetre
            for event in pygame.event.get():
                # si l'event est fermeture de fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    # détecter si un joueur lache une touche du clavier
                elif event.type == pygame.KEYDOWN:
                    self.game.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        if self.game.is_playing:
                            self.game.player.launch_projectile()
                        else:
                            # mettre le jeu en mode lancé
                            self.game.start()
                            self.game.sound_manager.play('click')

                elif event.type == pygame.KEYUP:  # si la touche n'est plus utilisé
                    self.game.pressed[event.key] = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # verification poru savoir si la souris est en collision avec le button jouer
                    if self.play_button_rect.collidepoint(event.pos):
                        # mettre le jeu en mode lancé
                        self.game.start()
                        self.game.sound_manager.play('click')
                        if self.game.is_playing:
                            pygame.MOUSEBUTTONDOWN = False
            # fixer le nombre de fps
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
