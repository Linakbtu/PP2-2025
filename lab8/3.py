import pygame
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint Program")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = BLACK

drawing = False
draw_shape = "line"  
last_pos = (0, 0)
line_width = 5
eraser_size = 20  

shapes = []

def random_color():
    return random.choice([BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if draw_shape == "line":
                shapes.append(("line", color, last_pos, pygame.mouse.get_pos()))
            elif draw_shape == "rectangle":
                shapes.append(("rectangle", color, last_pos, pygame.mouse.get_pos()))
            elif draw_shape == "circle":
                radius = int(((pygame.mouse.get_pos()[0] - last_pos[0])**2 + (pygame.mouse.get_pos()[1] - last_pos[1])**2)**0.5)
                shapes.append(("circle", color, last_pos, radius))
            elif draw_shape == "eraser":
                shapes.append(("eraser", WHITE, last_pos, pygame.mouse.get_pos()))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # 'r' for rectangle
                draw_shape = 'rectangle'
            elif event.key == pygame.K_c:  # 'c' for circle
                draw_shape = 'circle'
            elif event.key == pygame.K_e:  # 'e' for eraser
                draw_shape = 'eraser'
            elif event.key == pygame.K_b:  # 'b' for brush
                draw_shape = 'line'
            elif event.key == pygame.K_s:  # 's' for random color
                color = random_color()

    window.fill(WHITE)

    for shape in shapes:
        if shape[0] == "line":
            pygame.draw.line(window, shape[1], shape[2], shape[3], line_width)
        elif shape[0] == "rectangle":
            pygame.draw.rect(window, shape[1], pygame.Rect(shape[2], (shape[3][0] - shape[2][0], shape[3][1] - shape[2][1])), 3)
        elif shape[0] == "circle":
            pygame.draw.circle(window, shape[1], shape[2], shape[3], 3)
        elif shape[0] == "eraser":
            pygame.draw.line(window, shape[1], shape[2], shape[3], eraser_size)

    if drawing:
        if draw_shape == "line":
            pygame.draw.line(window, color, last_pos, pygame.mouse.get_pos(), line_width)
        elif draw_shape == "rectangle":
            pygame.draw.rect(window, color, pygame.Rect(last_pos, (pygame.mouse.get_pos()[0] - last_pos[0], pygame.mouse.get_pos()[1] - last_pos[1])), 3)
        elif draw_shape == "circle":
            radius = int(((pygame.mouse.get_pos()[0] - last_pos[0])**2 + (pygame.mouse.get_pos()[1] - last_pos[1])**2)**0.5)
            pygame.draw.circle(window, color, last_pos, radius, 3)
        elif draw_shape == "eraser":
            pygame.draw.line(window, WHITE, last_pos, pygame.mouse.get_pos(), eraser_size)
    pygame.display.update()
    pygame.time.Clock().tick(60)
