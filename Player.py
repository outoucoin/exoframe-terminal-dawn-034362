import pygame

class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))  # Avatar du joueur
        self.image.fill((0, 255, 0))  # Vert pour le joueur
        self.rect = self.image.get_rect(center=(400, 300))  # Position initiale
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()  # Vérifier les touches enfoncées
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed  # Déplacer à gauche
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed  # Déplacer à droite
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed  # Déplacer vers le haut
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed  # Déplacer vers le bas

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Dessiner le joueur sur l'écran