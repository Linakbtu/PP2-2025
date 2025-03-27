import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

WHITE = (255, 255, 255)
GOLD = (255, 223, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SPEED = 7

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)

coin_count = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 70)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def update(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        pygame.draw.circle(self.image, GOLD, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, WIDTH - 20), 0)

    def update(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > HEIGHT:
            self.kill()  

player = Player()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for _ in range(3):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if random.randint(1, 40) == 1:
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)

    all_sprites.update()

    if pygame.sprite.spritecollideany(player, enemies):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    collected = pygame.sprite.spritecollide(player, coins, True)
    coin_count += len(collected)

    all_sprites.draw(screen)

    coin_text = font.render(f"Coins: {coin_count}", True, BLACK)
    screen.blit(coin_text, (WIDTH - 120, 10))

    pygame.display.flip()
    clock.tick(60)
