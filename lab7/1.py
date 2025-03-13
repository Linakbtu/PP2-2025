import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 400,400
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60

background = pygame.image.load("mickeyClock.png")  
minute_hand = pygame.image.load("min_hand.png")   
second_hand = pygame.image.load("sec_hand.png")   

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (200, 20))
second_hand = pygame.transform.scale(second_hand, (200, 20))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec
    
    min_angle = - (minutes % 60) * 6  
    sec_angle = - (seconds % 60) * 6  
    
    rotated_minute_hand = pygame.transform.rotate(minute_hand, min_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, sec_angle)
    
    min_rect = rotated_minute_hand.get_rect(center=CENTER)
    sec_rect = rotated_second_hand.get_rect(center=CENTER)
    
    screen.blit(rotated_minute_hand, min_rect.topleft)
    screen.blit(rotated_second_hand, sec_rect.topleft)
    
    pygame.display.flip()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()