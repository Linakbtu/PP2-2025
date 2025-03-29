import pygame
import random

pygame.init()
w, h = 800, 600
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Mini Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = BLACK
font = pygame.font.SysFont("Arial", 14)

draw = False
tool = "brush"
start_pos = (0, 0)
shapes = []

def random_color():
    return random.choice([(0,0,0), (255,0,0), (0,255,0), (0,0,255)])

def help_panel():
    tools = [
        ("b", "Кисть"), ("r", "Прямоугольник"), ("s", "Квадрат"),
        ("c", "Круг"), ("t", "Треугольник"), ("h", "Ромб"),
        ("e", "Ластик"), ("x", "Цвет")
    ]
    y = 5
    for key, name in tools:
        txt = font.render(f"{key}: {name}", True, BLACK)
        win.blit(txt, (5, y))
        y += 15
    tool_txt = font.render(f"Инструмент: {tool}", True, BLACK)
    win.blit(tool_txt, (5, y + 5))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            start_pos = e.pos
        if e.type == pygame.MOUSEBUTTONUP:
            draw = False
            end = pygame.mouse.get_pos()
            shapes.append((tool, color, start_pos, end))
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_b: tool = "brush"
            if e.key == pygame.K_r: tool = "rect"
            if e.key == pygame.K_s: tool = "square"
            if e.key == pygame.K_c: tool = "circle"
            if e.key == pygame.K_t: tool = "tri"
            if e.key == pygame.K_h: tool = "rhomb"
            if e.key == pygame.K_e: tool = "eraser"
            if e.key == pygame.K_x: color = random_color()

    win.fill(WHITE)

    for t, col, a, b in shapes:
        if t == "brush": pygame.draw.line(win, col, a, b, 3)
        if t == "rect": pygame.draw.rect(win, col, pygame.Rect(a, (b[0]-a[0], b[1]-a[1])), 2)
        if t == "square":
            size = max(abs(b[0]-a[0]), abs(b[1]-a[1]))
            pygame.draw.rect(win, col, (a[0], a[1], size, size), 2)
        if t == "circle":
            r = int(((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5)
            pygame.draw.circle(win, col, a, r, 2)
        if t == "tri":
            points = [a, (b[0], b[1]), (a[0], b[1])]
            pygame.draw.polygon(win, col, points, 2)
        if t == "rhomb":
            cx, cy = (a[0]+b[0])//2, (a[1]+b[1])//2
            dx, dy = abs(b[0]-a[0])//2, abs(b[1]-a[1])//2
            pts = [(cx, cy-dy), (cx+dx, cy), (cx, cy+dy), (cx-dx, cy)]
            pygame.draw.polygon(win, col, pts, 2)
        if t == "eraser": pygame.draw.line(win, WHITE, a, b, 20)

    if draw:
        now = pygame.mouse.get_pos()
        if tool == "brush": pygame.draw.line(win, color, start_pos, now, 3)
        if tool == "rect":
            pygame.draw.rect(win, color, pygame.Rect(start_pos, (now[0]-start_pos[0], now[1]-start_pos[1])), 2)
        if tool == "square":
            size = max(abs(now[0]-start_pos[0]), abs(now[1]-start_pos[1]))
            pygame.draw.rect(win, color, (start_pos[0], start_pos[1], size, size), 2)
        if tool == "circle":
            r = int(((now[0]-start_pos[0])**2 + (now[1]-start_pos[1])**2)**0.5)
            pygame.draw.circle(win, color, start_pos, r, 2)
        if tool == "tri":
            pts = [start_pos, (now[0], now[1]), (start_pos[0], now[1])]
            pygame.draw.polygon(win, color, pts, 2)
        if tool == "rhomb":
            cx, cy = (start_pos[0]+now[0])//2, (start_pos[1]+now[1])//2
            dx, dy = abs(now[0]-start_pos[0])//2, abs(now[1]-start_pos[1])//2
            pts = [(cx, cy-dy), (cx+dx, cy), (cx, cy+dy), (cx-dx, cy)]
            pygame.draw.polygon(win, color, pts, 2)
        if tool == "eraser":
            pygame.draw.line(win, WHITE, start_pos, now, 20)

    help_panel()
    pygame.display.update()
    pygame.time.Clock().tick(60)
