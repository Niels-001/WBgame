import pygame
import sys
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 20
ENEMY_SIZE = 30
BULLET_SIZE = 5
PLAYER_SPEED = 2
ENEMY_SPEED = 1
BULLET_SPEED = 4
ENEMY_COUNT = 9

SCORE_COUNT = 0

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down")

# Player setup
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_speed_x = 0
player_speed_y = 0

# Enemy setup
enemies = [pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(50, 300), ENEMY_SIZE, ENEMY_SIZE) for _ in range(ENEMY_COUNT)]

# Bullets setup
bullets = []

bullet_angle = -0.5 * math.pi

# Game loop
running = True
while running:
    time.sleep(0.005)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player_speed_x = 0
    player_speed_y = 0
    # Player movement
    if keys[pygame.K_a] and player.x >= 0:
        if keys[pygame.K_d]:
            player_speed_x = 0
            bullet_angle = 0.5 * math.pi
        else:
            player_speed_x = -PLAYER_SPEED
            bullet_angle = math.pi

    if keys[pygame.K_d] and player.x <= WIDTH-PLAYER_SIZE:
        if keys[pygame.K_a]:
            player_speed_x = 0
            bullet_angle = 0.5 * math.pi
        else:
            player_speed_x = PLAYER_SPEED
            bullet_angle = 0

    if keys[pygame.K_w] and player.y >= 0:
        player_speed_y = -PLAYER_SPEED
        bullet_angle = 1.5 * math.pi

    if keys[pygame.K_s] and player.y <= HEIGHT-PLAYER_SIZE:
        if keys[pygame.K_w]:
            player_speed_y = 0
        else:
            player_speed_y = PLAYER_SPEED
            bullet_angle = 0.5 * math.pi

    # Shooting (only one bullet at a time)
    if keys[pygame.K_SPACE] and len(bullets) == 0:
        if math.fabs(player_speed_y) == math.fabs(player_speed_x):
            bullet_velocity_x = BULLET_SPEED * math.cos(bullet_angle)
            bullet_velocity_y = BULLET_SPEED * math.sin(bullet_angle)
        bullet = pygame.Rect(player.centerx - BULLET_SIZE // 2, player.centery - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
        bullets.append(bullet)

    # Move player
    if math.fabs(player_speed_y) == math.fabs(player_speed_x):
        player.x += 0.5*(math.sqrt(2))*player_speed_x
        player.y += 0.5*(math.sqrt(2))*player_speed_y
    else:
        player.x += player_speed_x
        player.y += player_speed_y

    # Move enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.top > HEIGHT:
            enemy.y = random.randint(-100, -ENEMY_SIZE)
            enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)

    # Move bullets
    for bullet in bullets:
        bullet.x += BULLET_SPEED * math.cos(bullet_angle)
        bullet.y += BULLET_SPEED * math.sin(bullet_angle)

    # Remove bullets that are off-screen
    bullets = [bullet for bullet in bullets if bullet.colliderect(pygame.Rect(0, 0, WIDTH, HEIGHT))]

    # Collision detection
    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                SCORE_COUNT += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                enemy.y = random.randint(-100, -ENEMY_SIZE)
                enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)
                enemies.append(pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), -20, ENEMY_SIZE, ENEMY_SIZE))

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    pygame.display.update()

# Quit the game
pygame.quit()