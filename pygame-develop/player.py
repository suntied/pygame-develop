import pygame
from projectile import Projectile
import animation

#creer une premier class qui represente le premier joueur
class Player(animation.AnimateSprite):
      def __init__(self,game):
         super().__init__('player')
         self.game = game
         self.health = 100
         self.max_health = 100
         self.attack = 100
         self.velocity = 5
         self.rect = self.image.get_rect()
         self.rect.x = 400
         self.rect.y = 470
         self.all_projectiles = pygame.sprite.Group()
         self.isJump = False
         self.jumpCount = 10

      def damage(self,amount):
         if self.health - amount > amount:
            self.health -= amount
         else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

      def update_animation(self):
         self.animate()

      def update_health_bar(self,surface):
        #définir une couleur pour une jauge de vie
        bar_color = (111,210,46)
        #définir une couleur pour l'arriere plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)

        #definir la position de notre jauge de vie ainsi que sa largeur et son épaisseur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]

        #definir la position de l'arrière plan de notre jauge de vie 
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

      def launch_projectile(self):
         #creer une nouvelle instance de la classe projectile
         self.all_projectiles.add(Projectile(self))
         self.game.sound_manager.play('tir')

      def move_right(self):
         #demarrer l'animation 
         self.start_animation()
         # si le joueur n'est pas en collision avec un monstre
         if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

      def move_left(self):
         #demarrer l'animation 
         self.start_animation()
         self.rect.x -= self.velocity
             