"""Imports of important python libraries"""
import pygame  # for the UI, game mechanics and event handling
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


'''Creating a sprite group for Bullets '''
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
    Characters.draw(screen)


    '''Drawing all bullets and updating there movement'''
    for Bullet in Bullets:
        Bullet.update_bullets()

    Bullets.draw(screen)

    '''Game event handler'''
    key = pygame.key.get_pressed()  # Calling a built-in function that checks for any keys being pressed

    '''Update the Players. positions of both players, shooting actions and creating bullets'''
    Player_1.update(key, Bullets, Characters)
    Player_2.update(key, Bullets, Characters)

    '''Update the positions of all NPC's'''
    NPC_1.update(key, Bullets, Characters)
    NPC_2.update(key, Bullets, Characters)
    NPC_3.update(key, Bullets, Characters)
    NPC_4.update(key, Bullets, Characters)
    NPC_5.update(key, Bullets, Characters)

    '''Bails out of the game loop if the user closes the application'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    '''Updating the screen (every frame)'''
    pygame.display.update()

'''Quits the pygame module when the program has finished; after the game loop has stopped'''
pygame.quit()
