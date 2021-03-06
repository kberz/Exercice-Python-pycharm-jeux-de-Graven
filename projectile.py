import pygame

#Définir la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de cette class
    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 126
        self.rect.y = player.rect.y + 93
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile lorsceque ce dernier est en déplacement
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #Vérifier si notre projectile ne rencontre pas de monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)

        #Vérifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()

