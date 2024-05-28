# traffic_light.py
import pygame

class TrafficLight(pygame.sprite.Sprite):
    def __init__(self, x, y, state):
        super().__init__()
        self.image = pygame.Surface((20, 60))
        self.state = state  # 'red', 'yellow', 'green'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.update_color()

    def update_color(self):
        if self.state == 'red':
            self.image.fill((255, 0, 0))
        elif self.state == 'yellow':
            self.image.fill((255, 255, 0))
        elif self.state == 'green':
            self.image.fill((0, 255, 0))

    def update(self):
        # Update the light state here
        pass
