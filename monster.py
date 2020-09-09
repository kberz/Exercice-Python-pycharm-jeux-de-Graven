import pygame


#Créer une classe qui va pouvoir gérér la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):
    #ajouter le constructeur
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 426
        self.velocity = 5


    def forward(self):
        #Le déplacement du monstre pourra se faire uniquement si le groupe de joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity