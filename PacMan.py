import pygame
import random

# Ініціалізація pygame
pygame.init()

# Розміри екрану
screen_width = 600
screen_height = 400

# Встановлення екрану
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pac-Man')

# Визначення кольорів
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Властивості гравця
player_size = 20
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Властивості привидів
ghost_size = 20
ghost_speed = 3

# Список привидів
ghosts = []

# Додавання привидів
for _ in range(4):
    ghost_x = random.randint(0, screen_width - ghost_size)
    ghost_y = random.randint(0, screen_height - ghost_size)
    ghosts.append([ghost_x, ghost_y])

# Основний цикл гри
running = True
while running:
    # Встановлення FPS
    pygame.time.delay(100)

    # Відстеження подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отримання клавіш для керування гравцем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Запобігання виходу гравця за межі екрану
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_size:
        player_x = screen_width - player_size
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_size:
        player_y = screen_height - player_size

    # Переміщення привидів
    for ghost in ghosts:
        if ghost[0] < player_x:
            ghost[0] += ghost_speed
        elif ghost[0] > player_x:
            ghost[0] -= ghost_speed

        if ghost[1] < player_y:
            ghost[1] += ghost_speed
        elif ghost[1] > player_y:
            ghost[1] -= ghost_speed

    # Перевірка на зіткнення
    for ghost in ghosts:
        if abs(player_x - ghost[0]) < player_size and abs(player_y - ghost[1]) < player_size:
            running = False  # Гра закінчена, якщо Pac-Man зіткнеться з привидом

    # Очищення екрану
    screen.fill(BLACK)

    # Малювання Pac-Man
    pygame.draw.circle(screen, YELLOW, (player_x + player_size // 2, player_y + player_size // 2), player_size // 2)

    # Малювання привидів
    for ghost in ghosts:
        pygame.draw.rect(screen, BLUE, (ghost[0], ghost[1], ghost_size, ghost_size))

    # Оновлення екрану
    pygame.display.update()

# Закриття pygame
pygame.quit()
