import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Circles")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE

snake = [(5, 5)]
direction = (1, 0) 
food = None
score = 0
level = 1
speed = 10

def generate_food():
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake:
            return pos

food = generate_food()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (head[0] < 0 or head[0] >= cols or head[1] < 0 or head[1] >= rows or
        head in snake):
        print("Game Over")
        pygame.quit()
        sys.exit()

    snake.insert(0, head)

    if head == food:
        score += 1
        food = generate_food()

        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    fx, fy = food
    pygame.draw.circle(screen, RED, (fx * CELL_SIZE, fy * CELL_SIZE), CELL_SIZE // 2)

    for i, (x, y) in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.circle(screen, color, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed) 

pygame.quit()
