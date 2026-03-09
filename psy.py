import pygame
import math

pygame.init()

info = pygame.display.Info()
w, h = info.current_w, info.current_h

screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
clock = pygame.time.Clock()

time = 0

def draw_tree(x, y, angle, depth, length, hue, spread):
    if depth == 0:
        return

    x2 = x + math.cos(angle) * length
    y2 = y - math.sin(angle) * length

    color = pygame.Color(0)
    color.hsva = (hue % 360, 80, 100, 100)

    pygame.draw.line(screen, color, (x, y), (x2, y2), max(1, depth))

    new_len = length * 0.75

    draw_tree(x2, y2, angle - spread, depth - 1, new_len, hue + 8, spread)
    draw_tree(x2, y2, angle + spread, depth - 1, new_len, hue + 8, spread)


running = True

while running:

    screen.fill((5, 5, 10))

    mx, my = pygame.mouse.get_pos()

    spread = (mx / w) * math.pi
    base_length = (h / 4.5) * (my / h + 0.5)

    animated_spread = spread + math.sin(time) * 0.3

    draw_tree(
        w // 2,
        h - 50,
        math.pi / 2,
        11,
        base_length,
        time * 40,
        animated_spread
    )

    time += 0.02

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()