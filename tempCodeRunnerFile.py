import pygame
import sys
from queue import PriorityQueue

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Pathfinding Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Car properties
CAR_SIZE = 20
car_pos = [50, 50]
car_speed = 5

# Target position
target_pos = [700, 500]

# Grid properties
GRID_SIZE = 20
ROWS = HEIGHT // GRID_SIZE
COLS = WIDTH // GRID_SIZE

# Obstacles
obstacles = {(15, 20), (15, 21), (15, 22), (16, 23), (17, 25), (15, 24)}

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(WIN, BLACK, (0, y), (WIDTH, y))

def draw_car(position):
    pygame.draw.rect(WIN, RED, (*position, CAR_SIZE, CAR_SIZE))

def draw_target(position):
    pygame.draw.rect(WIN, GREEN, (*position, CAR_SIZE, CAR_SIZE))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(WIN, BLUE, (obstacle[0] * GRID_SIZE, obstacle[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < COLS and 0 <= neighbor[1] < ROWS and neighbor not in obstacles:
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    open_set.put((f_score[neighbor], neighbor))
    
    return []

def move_car(path):
    if path:
        next_pos = path.pop(0)
        car_pos[0] = next_pos[0] * GRID_SIZE
        car_pos[1] = next_pos[1] * GRID_SIZE

def main():
    path = a_star_search((car_pos[0] // GRID_SIZE, car_pos[1] // GRID_SIZE),
                         (target_pos[0] // GRID_SIZE, target_pos[1] // GRID_SIZE))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Move the car along the path
        move_car(path)
        
        # Drawing
        WIN.fill(WHITE)
        draw_grid()
        draw_car(car_pos)
        draw_target(target_pos)
        draw_obstacles()
        
        pygame.display.flip()
        clock.tick(10)  # Control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
