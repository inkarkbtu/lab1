import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размер ячейки и сетки
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

# Окно игры
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Levels and Timed Foods")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.SysFont('Arial', 20)

# Начальные параметры змейки
snake = [(5, 5)]
direction = (1, 0)  # Движение вправо

# Словарь для хранения еды
foods = {}

# Функция генерации еды
def spawn_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake and pos not in foods:
            weight = random.choice([1, 2, 3])  # Случайный вес еды
            timer = pygame.time.get_ticks()   # Время появления еды
            foods[pos] = (weight, timer)
            break

# Начальная еда
spawn_food()

score = 0
level = 1
speed = 10
clock = pygame.time.Clock()
FOOD_LIFETIME = 5000  # Еда исчезает через 5 секунд

while True:
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    # Новая позиция головы змейки
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Проверка на столкновение с собой или стенами
    if (
        new_head in snake or
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT
    ):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Обновление положения змейки
    snake.insert(0, new_head)

    # Проверка на съедание еды
    if new_head in foods:
        weight, _ = foods[new_head]
        score += weight
        del foods[new_head]

        # Повышение уровня каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2

        # Генерация новой еды
        spawn_food()
    else:
        snake.pop()  # Если еда не съедена — удаляется хвост

    # Удаление еды по истечению времени
    current_time = pygame.time.get_ticks()
    expired_foods = [pos for pos, (_, t) in foods.items() if current_time - t > FOOD_LIFETIME]
    for pos in expired_foods:
        del foods[pos]
        spawn_food()

    # Отрисовка еды
    for pos, (weight, _) in foods.items():
        color = RED if weight == 1 else (255, 100, 0) if weight == 2 else (255, 255, 0)
        pygame.draw.rect(win, color, (pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Отрисовка змейки
    for idx, segment in enumerate(snake):
        color = GREEN if idx == 0 else DARK_GREEN
        pygame.draw.rect(win, color, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    win.blit(score_text, (10, 10))

    # Обновление экрана и скорость игры
    pygame.display.update()
    clock.tick(speed)