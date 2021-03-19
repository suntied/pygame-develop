import pygame
from game import Game
import math

pygame.init()

#

#définir une clock 
clock = pygame.time.Clock()
FPS = 60

#générer la fenetre du jeu
pygame.display.set_caption("World War Worms")
screen = pygame.display.set_mode((1080,720))

#Charger l'arrière plan
background = pygame.image.load('assets/background.jpg')

#importer charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

game = Game()

#boucle tant que cette condition est vrai
running = True
while running:
    #tant que le jeu est actif

    #arrière plan
    screen.blit(background,(0,0))

    #verifier si notre jeu a commencé
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    else:
        #ajouté mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)
        
    #mettre à jour l'ecran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #si l'event est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            #détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True               
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    #mettre le jeu en mode lancé
                    game.start()
                    game.sound_manager.play('click')
                    
        elif event.type == pygame.KEYUP: #si la touche n'est plus utilisé
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification poru savoir si la souris est en collision avec le button jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()
                game.sound_manager.play('click')
                if game.is_playing:
                    pygame.MOUSEBUTTONDOWN = False
    #fixer le nombre de fps
    clock.tick(FPS)


 