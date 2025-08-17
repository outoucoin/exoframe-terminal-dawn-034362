import pygame

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))  # Avatar de l'ennemi
        self.image.fill((255, 0, 0))  # Rouge pour l'ennemi
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self):
        self.rect.y += self.speed  # Déplacer l'ennemi vers le bas

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Dessiner l'ennemi sur l'écran