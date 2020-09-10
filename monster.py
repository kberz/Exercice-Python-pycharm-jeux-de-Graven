import pygame
import random

#Créer une classe qui va pouvoir gérér la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):
    #ajouter le constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        #Infliger les dégats
        self.health -= amount

        #Vérifier si sont nombre de vie est >=0
        if self.health <= 0:
            #réaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):

        #Désiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 15, self.rect.y - 10, self.health, 5])

    def forward(self):
        #Le déplacement du monstre pourra se faire uniquement si le groupe de joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre ne peut plus se déplacer alors il inflige des dégats
        else:
            #infliger des dégats
            self.game.player.damage(self.attack)