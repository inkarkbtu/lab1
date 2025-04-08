import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений
player_img = pygame.image.load("/Users/inkarbahytkali/Desktop/lab9/image/player.png")
enemy_img = pygame.image.load("//Users/inkarbahytkali/Desktop/lab9/image/enemy.png")
coin_img = pygame.image.load("/Users/inkarbahytkali/Desktop/lab9/image/coin.jpg")

# Получаем размеры объектов
player_width, player_height = player_img.get_size()
enemy_width, enemy_height = enemy_img.get_size()
coin_width, coin_height = coin_img.get_size()

# Позиция игрока
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Позиция врага
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 5  # начальная скорость врага

# Монеты
coins = []
coin_weights = [1, 2, 3]  # веса монет

# Счёт
score = 0
font = pygame.font.SysFont(None, 30)

# Увеличения скорости врага
COINS_TO_SPEED_UP = 5
next_speed_up = COINS_TO_SPEED_UP

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Движение врага
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(0, WIDTH - enemy_width)

    # Рандомный шанс появления новой монеты
    if random.randint(1, 50) == 1:  
        coin_x = random.randint(0, WIDTH - coin_width)
        coin_y = -coin_height
        coin_weight = random.choice(coin_weights)
        coins.append({"x": coin_x, "y": coin_y, "weight": coin_weight})

    # Движение и отрисовка монет
    for coin in coins[:]:
        coin["y"] += 4  
        screen.blit(coin_img, (coin["x"], coin["y"]))

        # Столкновение с игроком
        if (
            player_x < coin["x"] + coin_width and
            player_x + player_width > coin["x"] and
            player_y < coin["y"] + coin_height and
            player_y + player_height > coin["y"]
        ):
            score += coin["weight"]
            coins.remove(coin)

            # Увеличение скорости врага 
            if score >= next_speed_up:
                enemy_speed += 1
                next_speed_up += COINS_TO_SPEED_UP

        # Удаляем монету, если она вышла за экран
        elif coin["y"] > HEIGHT:
            coins.remove(coin)

    # Проверка столкновения с врагом
    if (
        player_x < enemy_x + enemy_width and
        player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and
        player_y + player_height > enemy_y
    ):
        print("Game Over!")
        running = False

    # Отрисовка объектов
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Отображение счёта в правом верхнем углу
    score_text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()