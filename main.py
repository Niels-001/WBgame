"""Imports of important python libraries"""
import pygame  # for the UI, game mechanics and event handling
import time  # for all time related commands
import Object_setup as Ob  # importing the setup file we made ourselves

'''Initiating pygame'''
pygame.init()

'''Setting up the framerate'''
clock = pygame.time.Clock()
FPS = 60

'''Setting up the game window'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BoxHead")

'''Creating a sprite group for for the player and NPC objects'''
Characters = pygame.sprite.Group()

'''Creating the player objects'''
player_1 = Ob.Character("Blue", 300, 300, 1)
player_2 = Ob.Character("Red", 500, 300, 2)

'''Creating the NPC objects'''
NPC_1 = Ob.Character('Black', player=0)
NPC_2 = Ob.Character('Black', player=0)
NPC_3 = Ob.Character('Black', player=0)
NPC_4 = Ob.Character('Black', player=0)
NPC_5 = Ob.Character('Black', player=0)

'''Adding the players and NPC's to the characters list'''
Characters.add(player_1, player_2, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5)

'''Creating the game loop'''
run = True
while run:
    clock.tick(FPS)
    screen.fill("beige")

    '''Drawing players and NPC's'''
    Characters.update()
    Characters.draw(screen)

    '''Game event handler'''
    key = pygame.key.get_pressed()  # Calling a built-in function that checks for any keys being pressed

    player_1.update_move(key)       # Movement controls for player 1

    player_2.update_move(key)       # Movement controls for player 2

    '''Making the program quit when the user closes the application'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    '''Updating the screen (every frame)'''
    pygame.display.update()

pygame.quit()