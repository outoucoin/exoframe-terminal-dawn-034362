import pygame
from GameManager import GameManager

# Initialisation de Pygame
pygame.init()

# Créer une instance de GameManager et démarrer le jeu
if __name__ == '__main__':
    game = GameManager()
    game.run()