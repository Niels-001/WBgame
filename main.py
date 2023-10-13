'''Imports of important python libraries
'''
import pygame   #for the UI, game mechanics and event handeling
import time     #for all time related commands
import Object_setup as Ob



pygame.init()   #initiate pygame

#frame rate
clock = pygame.time.Clock()
FPS = 60

'''GAME Window
'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BoxHead")

'''game variables, and functions'''
#create sprite group for squares
Characters = pygame.sprite.Group()

#create square and add to squares group
player_1 = Ob.Character("Blue", 500, 300, 1)
player_2 = Ob.Character("Red", 300, 300, 2)

NPC_1 = Ob.Character('Black', player = 0)
NPC_2 = Ob.Character('Black', player = 0)
NPC_3 = Ob.Character('Black', player = 0)
NPC_4 = Ob.Character('Black', player = 0)
NPC_5 = Ob.Character('Black', player = 0)

Characters.add(player_1, player_2, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5)


'''GAME Loop
'''
run = True
while run:
    clock.tick(FPS)
    screen.fill("beige")
    '''Draw playing field & assets'''


    '''Draw players & NPC's'''
    Characters.update()
    Characters.draw(screen)

    '''GAME Event Handler
    '''
    key = pygame.key.get_pressed()
    #movement controls player 1
    player_1.update_move(key)
    #movement controls player 2
    player_2.update_move(key)


    '''GAME menu & quit'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
