import pygame
import math
from game import Game
pygame.init()

#Générer la fenetre de notre jeu

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Importer une image de fond
background = pygame.image.load('assets/bg.jpg')

#Importer charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer ou charger notre boutton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
#Charger notre jeu
game = Game()

running = True

#Boucle tant que cette condition est vraie
while running:

    #appliquer l'arrière plan du jeu
    screen.blit(background, (0, -240))

    #Verifier si notre jeu a commencer ou non
    if game.is_playing:
        #Déclancher les instructions de la partie
        game.update(screen)
    #Vérifier si notre jeu n'as pas commencer
    else:
        #ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


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

            #détecter si la touche espace est activé
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Vérification pour savoir si la souris est en collision avec le boutton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()