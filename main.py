import pygame
from game import Game
pygame.init()

#Générer la fenetre de notre jeu

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 600))

#Importer une image de fond
background = pygame.image.load('assets/bg.jpg')

#Charger notre jeu
game = Game()

running = True

#Boucle tant que cette condition est vraie
while running:

    #appliquer l'arrière plan du jeu
    screen.blit(background, (0, -330))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    #Verifier les touches droite ou gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    #mettre a jour notre écran
    pygame.display.flip()

    #Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
