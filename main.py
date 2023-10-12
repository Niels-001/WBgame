# Imports of important python libraries
import pygame   # for the UI, game mechanics and event handling
import time     # for all time related commands
import Object_setup as Ob

pygame.init()   # initiate pygame

# frame rate
clock = pygame.time.Clock()
FPS = 60

# Game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BoxHead")

'''game variables, and functions'''
# create sprite group for squares
Characters = pygame.sprite.Group()

# create square and add to squares group
player_1 = Ob.Character("Blue", 300, 300)
player_2 = Ob.Character("Red", 500, 300)

Characters.add(player_1, player_2)

# Game Loop
run = True
while run:
    clock.tick(FPS)
    screen.fill("beige")
    '''Draw playing field & assets'''

    '''Draw players & NPC's'''
    Characters.update()
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT), 3)
    Characters.draw(screen)

    '''GAME Event Handler'''

    Ob.Character.inputs(player_1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    Ob.Character.inputs(player_2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    '''GAME menu & quit'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
