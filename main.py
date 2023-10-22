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

'''Creating a sprite groups for: the player and NPC objects, assets and guns, '''
Characters = pygame.sprite.Group()
Assets = pygame.sprite.Group()

'''Creating a list and sprite group '''
Bullets = pygame.sprite.Group()

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

'''Creating the game loop'''
run = True
while run:
    clock.tick(FPS)
    screen.fill("beige")

    '''Drawing players and NPC's'''
    Characters.update()
    Characters.draw(screen)

    '''Drawing all assets and guns'''
    Assets.update()
    Assets.draw(screen)

    '''Drawing all bullets and updating there movement'''
    for Bullet in Bullets:
        Bullet.update()

    Bullets.draw(screen)

    '''Game event handler'''
    key = pygame.key.get_pressed()  # Calling a built-in function that checks for any keys being pressed

    # if key[pygame.K_SPACE]:
    #     Bullets.add(Pistol.shoot())

    checks1 = [Player_2.rect, NPC_1.rect, NPC_2.rect, NPC_3.rect, NPC_4.rect, NPC_5.rect]
    checks2 = [Player_1.rect, NPC_1.rect, NPC_2.rect, NPC_3.rect, NPC_4.rect, NPC_5.rect]

    checks3 = [Player_1.rect, Player_2.rect, NPC_2.rect, NPC_3.rect, NPC_4.rect, NPC_5.rect]
    checks4 = [Player_1.rect, Player_2.rect, NPC_1.rect, NPC_3.rect, NPC_4.rect, NPC_5.rect]
    checks5 = [Player_1.rect, Player_2.rect, NPC_1.rect, NPC_2.rect, NPC_4.rect, NPC_5.rect]
    checks6 = [Player_1.rect, Player_2.rect, NPC_1.rect, NPC_2.rect, NPC_3.rect, NPC_5.rect]
    checks7 = [Player_1.rect, Player_2.rect, NPC_1.rect, NPC_2.rect, NPC_3.rect, NPC_4.rect]

    '''Update the positions of both players'''
    Player_1.inputs(key, checks1, checks2)
    Player_2.inputs(key, checks1, checks2)

    if Player_1.shoot(key):
        Bullets.add(Player_1.shoot(key))
    if Player_2.shoot(key):
        Bullets.add(Player_2.shoot(key))

    '''Update the positions of all NPC's'''
    NPC_1.npc_movement(NPC_1.get_closest_player(Player_1, Player_2))
    NPC_2.npc_movement(NPC_2.get_closest_player(Player_1, Player_2))
    NPC_3.npc_movement(NPC_3.get_closest_player(Player_1, Player_2))
    NPC_4.npc_movement(NPC_4.get_closest_player(Player_1, Player_2))
    NPC_5.npc_movement(NPC_5.get_closest_player(Player_1, Player_2))

    print("next frame")

    '''Bails out of the game loop if the user closes the application'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    '''Updating the screen (every frame)'''
    pygame.display.update()

'''Quits the pygame module when the program has finished; after the game loop has stopped'''
pygame.quit()
