import pygame
import random
import sys
import time

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Circles")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Основные переменные
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE

# Состояние змейки
snake = [(5, 5)]
direction = (1, 0)
score = 0
level = 1
speed = 10

# Структура еды: позиция, вес, цвет, время появления
food = None
food_timer = 0  # в секундах
food_lifetime = 5  # через сколько секунд еда исчезнет

# Типы еды с разными весами и цветами
food_types = [
    {'weight': 1, 'color': RED},
    {'weight': 2, 'color': YELLOW},
    {'weight': 3, 'color': BLUE}
]

def generate_food():
    """Создает еду в случайной позиции, не совпадающей со змейкой"""
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake:
            food_type = random.choice(food_types)
            return {
                'position': pos,
                'weight': food_type['weight'],
                'color': food_type['color'],
                'time': time.time()
            }

# Генерируем первую еду
food = generate_food()

# Основной цикл игры
running = True
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление направлением змейки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    # Передвигаем голову змейки
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка на столкновение со стеной или с собой
    if (head[0] < 0 or head[0] >= cols or
        head[1] < 0 or head[1] >= rows or
        head in snake):
        print("Game Over")
        pygame.quit()
        sys.exit()

    snake.insert(0, head)

    # Проверка на съедание еды
    if head == food['position']:
        score += food['weight']
        if score % 3 == 0:
            level += 1
            speed += 2
        food = generate_food()
    else:
        snake.pop()

    # Проверка на истечение времени жизни еды
    if time.time() - food['time'] > food_lifetime:
        food = generate_food()

    # Отрисовка еды
    fx, fy = food['position']
    pygame.draw.circle(screen, food['color'],
                       (fx * CELL_SIZE + CELL_SIZE // 2,
                        fy * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 2)

    # Отрисовка змейки
    for i, (x, y) in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.circle(screen, color,
                           (x * CELL_SIZE + CELL_SIZE // 2,
                            y * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 2)

    # Вывод счета и уровня
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
