import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Визначаємо розміри екрану
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Налаштування кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS (кадри на секунду)
clock = pygame.time.Clock()

# Завантаження зображень автомобіля
car_width = 50
car_img = pygame.image.load('car.png')  # Замініть на шлях до вашого зображення


def draw_car(x, y):
    screen.blit(car_img, (x, y))


# Основна функція гри
def game_loop():
    car_x = (screen_width * 0.45)
    car_y = (screen_height * 0.8)
    car_x_change = 0

    # Параметри перешкод
    obstacle_start_x: int = random.randrange(0, screen_width - car_width)
    obstacle_start_y = -600
    obstacle_speed = 7
    obstacle_width = 100
    obstacle_height = 100

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Обробка натискань клавіш для керування автомобілем
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                if event.key == pygame.K_RIGHT:
                    car_x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        # Оновлення позиції автомобіля
        car_x += car_x_change

        # Заповнюємо екран фоном
        screen.fill(WHITE)

        # Малюємо перешкоди
        pygame.draw.rect(screen, BLACK, [obstacle_start_x, obstacle_start_y, obstacle_width, obstacle_height])
        obstacle_start_y += obstacle_speed

        # Малюємо автомобіль
        draw_car(car_x, car_y)

        # Відслідковуємо зіткнення
        if car_x > screen_width - car_width or car_x < 0:
            game_over = True

        if obstacle_start_y > screen_height:
            obstacle_start_y = 0 - obstacle_height
            obstacle_start_x = random.randrange(0, screen_width - car_width)

        if car_y < obstacle_start_y + obstacle_height:
            if obstacle_start_x < car_x < obstacle_start_x + obstacle_width or obstacle_start_x < car_x + car_width < obstacle_start_x + obstacle_width:
                game_over = True

        # Оновлюємо екран
        pygame.display.update()

        # Кількість кадрів на секунду
        clock.tick(60)

    pygame.quit()
    quit()


game_loop()
