import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20  # Size of each cell in the grid
COLUMNS = SCREEN_WIDTH // GRID_SIZE
ROWS = SCREEN_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (40, 40, 40)
ROAD_COLOR = (128, 128, 128)
NOT_ROAD_COLOR = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grid Map")

# Create the grid (2D list) and initialize all cells as "not road"
grid = [["not road" for _ in range(COLUMNS)] for _ in range(ROWS)]

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if grid[row][col] == "road":
                color = ROAD_COLOR
            else:
                color = NOT_ROAD_COLOR
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            # pygame.draw.rect(screen, WHITE, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

# Car class
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * GRID_SIZE  # Mengkonversi posisi x dari grid cells ke piksel
        self.rect.y = y * GRID_SIZE  # Mengkonversi posisi y dari grid cells ke piksel
        self.initspeed = speed
        self.speed = speed  # Kecepatan awal mobil
        self.direction = (1, 0)  # Arah awal (ke kanan)

    def update(self, other_cars):
        # Check for other cars in the same lane and in front of this car
        next_x = (self.rect.x + self.speed * self.direction[0]) % SCREEN_WIDTH
        next_y = (self.rect.y + self.speed * self.direction[1]) % SCREEN_HEIGHT
        next_col = next_x // GRID_SIZE
        next_row = next_y // GRID_SIZE

        # Check if the next cell is a road and there are no other cars there
        if grid[next_row][next_col] == "road" and not any(c.rect.collidepoint(next_x + 60, next_y) for c in other_cars if c != self):
            # Accelerate
            self.speed = min(self.speed + 1, self.initspeed)  # Increase speed (up to maximum of 5)
        else:
            # Slow down
            self.speed = max(self.speed - 1, 1)  # Decrease speed (minimum speed of 1)

        # Move the car
        self.dx = self.speed * self.direction[0]
        self.dy = self.speed * self.direction[1]
        self.rect.x = (self.rect.x + self.dx) % SCREEN_WIDTH
        self.rect.y = (self.rect.y + self.dy) % SCREEN_HEIGHT

start_row = 4
end_row = 26
start_col = 4
end_col = 36

# Define road paths
for i in range(start_col, end_col):
    grid[4][i] = "road"
    grid[25][i] = "road"
    grid[ROWS//2][i] = "road"

for i in range(start_row, end_row):
    grid[i][4] = "road"
    grid[i][35] = "road"
    grid[i][COLUMNS//2] = "road"

# Function to find a random road cell
def find_road():
    road_cells = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            if grid[i][j] == "road":
                road_cells.append((i, j))
    return random.choice(road_cells)

# Find initial positions for cars on the road
car1_pos = find_road()
car2_pos = find_road()

# Create cars at the found positions
car1 = Car(car1_pos[1], car1_pos[0], 5)  # Menggunakan posisi acak di jalan dan kecepatan 5
car2 = Car(car2_pos[1], car2_pos[0], 2)  # Menggunakan posisi acak di jalan dan kecepatan 2

# All sprites group
all_sprites = pygame.sprite.Group()
all_sprites.add(car1, car2)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update cars movement
    all_sprites.update([car1, car2])  # Pass list of all cars to update method

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    draw_grid()

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
