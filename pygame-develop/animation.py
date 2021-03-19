import pygame

#definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0 #commencer l'anim à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    #methode pour animer le sprite
    def animate(self,loop=False):
        if self.animation:
            #passer à l'image suivante
            self.current_image += 1  #randint de 0 ou 1 pour ralentir
            #verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    #desactivation de l'animation
                    self.animation = False
                    

            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image,self.size)

#charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #recup le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

#definir un dico qui va contenir les images charger de chaque sprite
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien'),
    'boss': load_animation_images('boss'),
    'bad_worms': load_animation_images('bad_worms')
}
