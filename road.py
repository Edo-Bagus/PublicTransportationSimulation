import pygame

class Road(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, direction, next_road=None):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((50, 50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction
        self.next_road = next_road

    def draw(self, screen):
        screen.blit(self.image, self.rect)