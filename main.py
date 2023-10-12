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
player_1 = Ob.Character("Blue", 500, 300)
player_2 = Ob.Character("Red", 300, 300)

Characters.add(player_1, player_2)


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
    # 4 keys pressed
    # print(key[pygame.K_a], key[pygame.K_d], key[pygame.K_w], key[pygame.K_s])

    if key[pygame.K_a] * key[pygame.K_d] * key[pygame.K_w] * key[pygame.K_s] :
        player_1.move(0,0)
    # 3 keys pressed
    elif key[pygame.K_a] * key[pygame.K_d] * key[pygame.K_w] :
        player_1.move(0,-1)
    elif key[pygame.K_a] * key[pygame.K_d] * key[pygame.K_s] :
        player_1.move(0, 1)
    elif key[pygame.K_a] * key[pygame.K_w] * key[pygame.K_s] :
        player_1.move(-1, 0)
    elif key[pygame.K_d] * key[pygame.K_w] * key[pygame.K_s] :
        player_1.move(1, 0)
    # 2 keys pressed
    elif key[pygame.K_a] and key[pygame.K_w]:
        player_1.move(-1, -1)
    elif key[pygame.K_a] * key[pygame.K_d] :
        player_1.move(0, 0)
    elif key[pygame.K_a] * key[pygame.K_s] :
        player_1.move(-1, 1)
    elif key[pygame.K_d] * key[pygame.K_w] :
        player_1.move(1, -1)
    elif key[pygame.K_d] * key[pygame.K_s] :
        player_1.move(1, 1)
    elif key[pygame.K_w] * key[pygame.K_s] :
        player_1.move(0, 0)
    # 1 key pressed
    elif key[pygame.K_a] :
        player_1.move(-1, 0)
    elif key[pygame.K_d] :
        player_1.move(1, 0)
    elif key[pygame.K_w] :
        player_1.move(0, -1)
    elif key[pygame.K_s]:
        player_1.move(0, 1)
    
    
    
    '''GAME menu & quit'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
