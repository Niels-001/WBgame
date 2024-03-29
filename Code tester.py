# # import pygame
# # import random
# #
# # pygame.init()
# #
# # #define screen size
# # SCREEN_WIDTH = 1000
# # SCREEN_HEIGHT = 600
# #
# # #colours
# # colours = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy"]
# #
# # #create game window
# # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# # pygame.display.set_caption("Sprite Groups")
# #
# # #frame rate
# # clock = pygame.time.Clock()
# # FPS = 60
# #
# # #create class for squares
# # class Square(pygame.sprite.Sprite):
# #   def __init__(self, col, x, y):
# #     pygame.sprite.Sprite.__init__(self)
# #     self.image = pygame.Surface((50, 50))
# #     self.image.fill(col)
# #     self.rect = self.image.get_rect()
# #     self.rect.center = (x, y)
# #
# #   def update(self):
# #     self.rect.move_ip(0, 5)
# #     # check if sprite has gone off screen
# #     if self.rect.top > SCREEN_HEIGHT:
# #       self.kill()
# #
# # #create sprite group for squares
# # squares = pygame.sprite.Group()
# #
# # #create square and add to squares group
# # square = Square("crimson", 500, 300)
# # squares.add(square)
# #
# # #game loop
# # run = True
# # while run:
# #
# #   clock.tick(FPS)
# #
# #   #update background
# #   screen.fill("cyan")
# #
# #   #update sprite group
# #   squares.update()
# #
# #   #draw sprite group
# #   squares.draw(screen)
# #
# #   print(squares)
# #
# #   #event handler
# #   for event in pygame.event.get():
# #     if event.type == pygame.MOUSEBUTTONDOWN:
# #       # get mouse coordinates
# #       pos = pygame.mouse.get_pos()
# #       # create square
# #       square = Square(random.choice(colours), pos[0], pos[1])
# #       squares.add(square)
# #     #quit program
# #     if event.type == pygame.QUIT:
# #       run = False
# #
# #   #update display
# #   pygame.display.flip()
# #
# # pygame.quit()
# #
# #
# #
# #
# # '''Imports of important python libraries
# # '''
# # import pygame as pg #for the UI, game mechanics and event handeling
# # import time     #for all time related commands
# # import random
# #
# # pg.init()   #initiate pg
# #
# # '''GAME Window
# # '''
# # SCREEN_WIDTH = 800
# # SCREEN_HEIGHT = 600
# #
# # screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# #
# # '''game variables, and functions'''
# # player = pg.Rect((300,250,20,20))
# #
# # '''GAME Loop
# # '''
# # run = True
# # while run:
# #     time.sleep(0.001)
# #
# #     '''Draw playing field & assets'''
# #     screen.fill((0,0,0))
# #
# #     '''Draw players & NPC's'''
# #     pg.draw.rect(screen, (255, 255, 255), player)
# #
# #     '''GAME Event Handler
# #     '''
# #     key = pg.key.get_pressed()
# #     if key[pg.K_a] == True:
# #         player.move_ip(-1,0)
# #     elif key[pg.K_d] == True:
# #         player.move_ip(1,0)
# #     elif key[pg.K_s] == True:
# #         player.move_ip(0, 1)
# #     elif key[pg.K_w] == True:
# #         player.move_ip(0, -1)
# #
# #     '''GAME menu & quit'''
# #     for event in pg.event.get():
# #         if event.type == pg.QUIT:
# #             run = False
# #
# #     pg.display.update()
# #
# # pg.quit()
#
# import pygame
#
# pygame.init()
#
# Screen = pygame.display.set_mode((500,500))
#
# # running = False
# # run = True
# # while run:
# #
# #     key = pygame.key.get_pressed()
# #     if key[pygame.K_a]*key[pygame.K_LSHIFT] == True:
# #         print("sprinting")
# #     elif key[pygame.K_a] == True:
# #         print("Running")
# #
# #
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False
#
#         # if event.type == pygame.KEYDOWN:
#         #     if event.key == pygame.K_a:
#         #         running = True
#         #
#         # if event.type == pygame.KEYUP:
#         #     if event.key == pygame.K_a:
#         #         running = False
#
#     # if running:
#     #     print('running')
#
# # pygame.quit()
#
# # map en collisions test Kobus 12/10
#
# import pygame
# import sys
# import random
# import math
# import time
# import numpy as np
#
# # Initialize Pygame
# pygame.init()
#
# # Constants
# WIDTH, HEIGHT = 800, 600
# PLAYER_SIZE = 20
# ENEMY_SIZE = 30
# BULLET_SIZE = 5
# PLAYER_SPEED = 2
# ENEMY_SPEED = 1
# BULLET_SPEED = 5
# ENEMY_COUNT = 9
#
# SCORE_COUNT = 0
#
# colliders = [{"x":WIDTH/5,"y":HEIGHT/5, "width":10,"height":10}]
#
# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)
#
# # Create the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Top-Down")
#
# # Map setup
#
# obstacles = [pygame.Rect(colliders[i]["x"],colliders[i]["y"],colliders[i]["width"],colliders[i]["height"])for i in range(len(colliders))]
#
# # Player setup
# player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
# player_speed_x = 0
# player_speed_y = 0
#
# # Enemy setup
# enemies = [pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(50, 300), ENEMY_SIZE, ENEMY_SIZE) for i in range(ENEMY_COUNT)]
#
# # Bullets setup
# bullets = []
#
# bullet_angle = -0.5 * math.pi
#
# # Game loop
# running = True
# while running:
#     time.sleep(0.005)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#
#     player_speed_x = 0
#     player_speed_y = 0
#     # Player movement
#     if keys[pygame.K_a] and player.x >= 0:
#         if keys[pygame.K_d]:
#             player_speed_x = 0
#             bullet_angle = 0.5 * math.pi
#         else:
#             player_speed_x = -PLAYER_SPEED
#             bullet_angle = math.pi
#
#     if keys[pygame.K_d] and player.x <= WIDTH-PLAYER_SIZE:
#         if keys[pygame.K_a]:
#             player_speed_x = 0
#             bullet_angle = 0.5 * math.pi
#         else:
#             player_speed_x = PLAYER_SPEED
#             bullet_angle = 0
#
#     if keys[pygame.K_w] and player.y >= 0:
#         player_speed_y = -PLAYER_SPEED
#         bullet_angle = 1.5 * math.pi
#
#     if keys[pygame.K_s] and player.y <= HEIGHT-PLAYER_SIZE:
#         if keys[pygame.K_w]:
#             player_speed_y = 0
#         else:
#             player_speed_y = PLAYER_SPEED
#             bullet_angle = 0.5 * math.pi
#
#     # Shooting (only one bullet at a time)
#     if keys[pygame.K_SPACE] and len(bullets) == 0:
#         if math.fabs(player_speed_y) == math.fabs(player_speed_x):
#             bullet_velocity_x = BULLET_SPEED * math.cos(bullet_angle)
#             bullet_velocity_y = BULLET_SPEED * math.sin(bullet_angle)
#         bullet = pygame.Rect(player.centerx - BULLET_SIZE // 2, player.centery - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
#         bullets.append(bullet)
#
#     # Move player
#     if math.fabs(player_speed_y) == math.fabs(player_speed_x):
#         player.x += 0.5*(math.sqrt(2))*player_speed_x
#         player.y += 0.5*(math.sqrt(2))*player_speed_y
#     else:
#         player.x += player_speed_x
#         player.y += player_speed_y
#
#     # Move enemies
#     for enemy in enemies:
#         enemy.y += ENEMY_SPEED
#         if enemy.top > HEIGHT:
#             enemy.y = random.randint(-100, -ENEMY_SIZE)
#             enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)
#
#     # Move bullets
#     for bullet in bullets:
#         bullet.x += BULLET_SPEED * math.cos(bullet_angle)
#         bullet.y += BULLET_SPEED * math.sin(bullet_angle)
#
#     # Remove bullets that are off-screen
#     bullets = [bullet for bullet in bullets if bullet.colliderect(pygame.Rect(0, 0, WIDTH, HEIGHT))]
#
#     # Collision detection
#     for enemy in enemies:
#         for bullet in bullets:
#             if enemy.colliderect(bullet):
#                 SCORE_COUNT += 1
#                 enemies.remove(enemy)
#                 # bullets.remove(bullet)
#                 enemy.y = random.randint(-100, -ENEMY_SIZE)
#                 enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)
#                 enemies.append(pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), -20, ENEMY_SIZE, ENEMY_SIZE))
#
#     # Draw everything
#     screen.fill(WHITE)
#     pygame.draw.rect(screen, RED, player)
#     for enemy in enemies:
#         pygame.draw.rect(screen, RED, enemy)
#     for bullet in bullets:
#         pygame.draw.rect(screen, RED, bullet)
#
#     pygame.display.update()
#
# obstacles = []
#
# # Quit the game
# pygame.quit()
#
# # def direction_closest_player(self, pl1, pl2):
#     #     """
#     #
#     #     :param pl1:
#     #     :param pl2:
#     #     :return:
#     #     """
#     #     diff1 = [pl1.rect.center[0] - self.rect.center[0], pl1.rect.center[1] - self.rect.center[1]]
#     #     diff2 = [pl2.rect.center[0] - self.rect.center[0], pl2.rect.center[1] - self.rect.center[1]]
#     #
#     #     dist1 = math.sqrt(diff1[0] ** 2 + diff1[1] ** 2)
#     #     dist2 = math.sqrt(diff2[0] ** 2 + diff2[1] ** 2)
#     #
#     #     ''' If player 1 is closer, return the direction from the NPC to that player. If either of the distances is
#     #             equal to zero, the direction will be zero in both directions, i.e. standing still'''
#     #     if dist1 != 0 and dist2 != 0:
#     #         if dist1 <= dist2:
#     #             return [diff1[0] / dist1, diff1[1] / dist1]
#     #         # If player 2 is closer, return the direction from the NPC to that player
#     #         elif dist2 < dist1:
#     #             return [diff2[0] / dist2, diff2[1] / dist2]
#     #     else:
#     #         return [0, 0]
import pygame

import Object_setup as Ob

Characters = pygame.sprite.Group()

'''Creating the player objects'''
Player_1 = Ob.Character("Blue", 300, 300, 1)
Player_2 = Ob.Character("Red", 500, 300, 2)

'''Creating the NPC objects'''
NPC_1 = Ob.Character((0, 0, 0), player=0)
NPC_2 = Ob.Character((50, 50, 50), player=0)
NPC_3 = Ob.Character((100, 100, 100), player=0)
NPC_4 = Ob.Character((150, 150, 150), player=0)
NPC_5 = Ob.Character((200, 200, 200), player=0)

# Pistol = Ob.Gun(300, 300, "pistol")

'''Adding the players and NPC's to the characters list'''
Characters.add(Player_1, Player_2, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5)

print(list(Characters)[1].rect.center)