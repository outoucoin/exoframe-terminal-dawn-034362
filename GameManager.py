import pygame
from Player import Player
from Enemy import Enemy

class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player()  # Créer un joueur
        self.enemies = [Enemy(x * 100, 50) for x in range(5)]  # Créer plusieurs ennemis
        self.running = True
        self.score = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Limiter à 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()  # Mettre à jour le joueur
        for enemy in self.enemies:
            enemy.update()  # Mettre à jour tous les ennemis

    def draw(self):
        self.screen.fill((0, 0, 0))  # Remplir l'arrière-plan
        self.player.draw(self.screen)  # Dessiner le joueur
        for enemy in self.enemies:
            enemy.draw(self.screen)  # Dessiner les ennemis
        pygame.display.flip()  # Mettre à jour l'affichage