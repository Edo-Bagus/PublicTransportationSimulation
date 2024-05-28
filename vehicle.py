import pygame

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, GRID_SIZE):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE
        self.rect.y = y * GRID_SIZE
        self.speed = 1

    def update(self, dx, dy):
        # Move the car
        new_x = self.rect.x + dx * GRID_SIZE
        new_y = self.rect.y + dy * GRID_SIZE

        # Check if the new position is within bounds and on a road cell
        if 0 <= new_x < SCREEN_WIDTH and 0 <= new_y < SCREEN_HEIGHT:
            new_col = new_x // GRID_SIZE
            new_row = new_y // GRID_SIZE
            if grid[new_row][new_col] == "road":
                self.rect.x = new_x
                self.rect.y = new_y