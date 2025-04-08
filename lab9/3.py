import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
current_color = BLACK

# Настройки
clock = pygame.time.Clock()
screen.fill(WHITE)
tool = "circle"  
start_pos = None  # стартовая точка рисования
radius = 20
eraser_size = 20

# Отрисовка кнопок для выбора цвета и инструмента
def draw_ui():
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 40))  
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i * 40, 5, 30, 30))
    pygame.draw.rect(screen, BLACK, (10 + colors.index(current_color) * 40, 5, 30, 30), 2)

running = True
while running:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Выбор цвета по клику на прямоугольник
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 40:
                for i, color in enumerate(colors):
                    if 10 + i * 40 <= x <= 40 + i * 40:
                        current_color = color
                continue
            start_pos = event.pos  

        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Рисуем фигуры в зависимости от выбранного инструмента
                if tool == "rect":
                    rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, current_color, rect, 2)

                elif tool == "square":
                    size = max(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, size, size)
                    pygame.draw.rect(screen, current_color, rect, 2)

                elif tool == "circle":
                    center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    radius = int(math.hypot(x2 - x1, y2 - y1) / 2)
                    pygame.draw.circle(screen, current_color, center, radius, 2)

                elif tool == "right_triangle":
                    pygame.draw.polygon(screen, current_color, [(x1, y1), (x1, y2), (x2, y2)], 2)

                elif tool == "equilateral_triangle":
                    side = x2 - x1
                    height = side * math.sqrt(3) / 2
                    pygame.draw.polygon(screen, current_color, [
                        (x1, y2),
                        (x2, y2),
                        ((x1 + x2) / 2, y2 - height)
                    ], 2)

                elif tool == "rhombus":
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    dx = abs(x2 - x1) // 2
                    dy = abs(y2 - y1) // 2
                    pygame.draw.polygon(screen, current_color, [
                        (center_x, center_y - dy),
                        (center_x + dx, center_y),
                        (center_x, center_y + dy),
                        (center_x - dx, center_y)
                    ], 2)

                start_pos = None

        # Рисование ластиком при зажатой кнопке мыши
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, eraser_size)

        # Переключение инструментов по клавишам
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_q:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()