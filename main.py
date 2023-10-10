'''Imports of important python libraries
'''
import pygame   #for the UI, game mechanics and event handeling
import time     #for all time related commands

pygame.init()   #initiate pygame

'''GAME Window
'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

'''game variables, and functions'''
player = pygame.Rect((300,250,20,20))

'''GAME Loop
'''
run = True
while run:
    time.sleep(0.001)

    '''Draw playing field & assets'''
    screen.fill((0,0,0))

    '''Draw players & NPC's'''
    pygame.draw.rect(screen, (255, 255, 255), player)

    '''GAME Event Handler
    '''
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)

    '''GAME menu & quit'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
