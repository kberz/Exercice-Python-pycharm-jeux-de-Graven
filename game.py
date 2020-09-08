import pygame
from player import Player

#Créer une seconde classe qui va représenter notre jeu
class Game:

    def __init__(self):
        #générer notre joueur
        self.player = Player()
        self.pressed = {}