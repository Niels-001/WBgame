# import pygame
# import random
#
# pygame.init()
#
# #define screen size
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 600
#
# #colours
# colours = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy"]
#
# #create game window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Sprite Groups")
#
# #frame rate
# clock = pygame.time.Clock()
# FPS = 60
#
# #create class for squares
# class Square(pygame.sprite.Sprite):
#   def __init__(self, col, x, y):
#     pygame.sprite.Sprite.__init__(self)
#     self.image = pygame.Surface((50, 50))
#     self.image.fill(col)
#     self.rect = self.image.get_rect()
#     self.rect.center = (x, y)
#
#   def update(self):
#     self.rect.move_ip(0, 5)
#     # check if sprite has gone off screen
#     if self.rect.top > SCREEN_HEIGHT:
#       self.kill()
#
# #create sprite group for squares
# squares = pygame.sprite.Group()
#
# #create square and add to squares group
# square = Square("crimson", 500, 300)
# squares.add(square)
#
# #game loop
# run = True
# while run:
#
#   clock.tick(FPS)
#
#   #update background
#   screen.fill("cyan")
#
#   #update sprite group
#   squares.update()
#
#   #draw sprite group
#   squares.draw(screen)
#
#   print(squares)
#
#   #event handler
#   for event in pygame.event.get():
#     if event.type == pygame.MOUSEBUTTONDOWN:
#       # get mouse coordinates
#       pos = pygame.mouse.get_pos()
#       # create square
#       square = Square(random.choice(colours), pos[0], pos[1])
#       squares.add(square)
#     #quit program
#     if event.type == pygame.QUIT:
#       run = False
#
#   #update display
#   pygame.display.flip()
#
# pygame.quit()
#
#
#
#
# '''Imports of important python libraries
# '''
# import pygame as pg #for the UI, game mechanics and event handeling
# import time     #for all time related commands
# import random
#
# pg.init()   #initiate pg
#
# '''GAME Window
# '''
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
#
# screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#
# '''game variables, and functions'''
# player = pg.Rect((300,250,20,20))
#
# '''GAME Loop
# '''
# run = True
# while run:
#     time.sleep(0.001)
#
#     '''Draw playing field & assets'''
#     screen.fill((0,0,0))
#
#     '''Draw players & NPC's'''
#     pg.draw.rect(screen, (255, 255, 255), player)
#
#     '''GAME Event Handler
#     '''
#     key = pg.key.get_pressed()
#     if key[pg.K_a] == True:
#         player.move_ip(-1,0)
#     elif key[pg.K_d] == True:
#         player.move_ip(1,0)
#     elif key[pg.K_s] == True:
#         player.move_ip(0, 1)
#     elif key[pg.K_w] == True:
#         player.move_ip(0, -1)
#
#     '''GAME menu & quit'''
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             run = False
#
#     pg.display.update()
#
# pg.quit()

import pygame

pygame.init()

Screen = pygame.display.set_mode((500,500))

# running = False
run = True
while run:

    key = pygame.key.get_pressed()
    if key[pygame.K_a]*key[pygame.K_LSHIFT] == True:
        print("sprinting")
    elif key[pygame.K_a] == True:
        print("Running")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         running = True
        #
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_a:
        #         running = False

    # if running:
    #     print('running')

pygame.quit()
