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

    #Actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    #récuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #récuperer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    #appliquer l'ensemble des images de mon groupe de projectile
    game.player.all_projectiles.draw(screen)

    #appliquer l'ensemble des images de mon groupe de monstre
    game.all_monsters.draw(screen)


    #Verifier les touches droite ou gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
