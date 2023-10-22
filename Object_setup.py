import pygame
import math
import random
import typing

'''THe Character class, creates objects for all characters Player and Non-player.
all characters get self.variables like movement speed, health location and size.
And they all get functions to move, and attack.'''


class Character(pygame.sprite.Sprite):
    def __init__(self, col, x=0, y=0, player=0, size=30):
        """
        :param col:
        :param x:
        :param y:
        :param player:
        """

        if player == 1:
            self.player = True
            self.controls = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE]
            self.ms = 5
        elif player == 2:
            self.player = True
            self.controls = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SLASH]
            self.ms = 5
        else:
            self.player = False
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            self.ms = 1

        # Create the Visual representation and hitboxes
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.Surface((size, size))
        self.image.fill(col)

        # set player position and direction
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = [1, 0]

        # Set up the weapons
        Pistol = Gun(self, 'pistol')
        UZI = Gun(self, 'UZI')
        self.weapons = {Pistol: 200, UZI: 0}
        self.active_weapon = Pistol

    def update(self, key, group, check):
        if self.player:
            self.player_movement(key, check)

            if key[pygame.K_1]:
                self.active_weapon = list(self.weapons.keys())[0]
            elif key[pygame.K_2]:
                self.active_weapon = list(self.weapons.keys())[1]
            elif key[pygame.K_0]:
                for weapon in self.weapons:
                    self.weapons[weapon] = 20

            self.update_gun(key, group)

    def get_closest_player(self, player_1, player_2):
        """This function returns the location of and the distance to the Player closest to this object.

        :param player_1: object, with a location
        :param player_2: object, with a location
        :return: Tuple(int(),int())
        """

        # Bereken de afstand naar beide spelers
        distance_1 = math.sqrt(abs(player_1.rect.center[0] - self.rect.center[0]) ** 2 + abs(
            player_1.rect.center[1] - self.rect.center[1]) ** 2)
        distance_2 = math.sqrt(abs(player_2.rect.center[0] - self.rect.center[0]) ** 2 + abs(
            player_2.rect.center[1] - self.rect.center[1]) ** 2)

        # Return de locatie van en afstand tot de dichtstbijzijnde speler
        if distance_1 > distance_2:
            return [player_2.rect.center, distance_2]
        elif distance_1 < distance_2:
            return [player_1.rect.center, distance_1]
        else:  # Als beide spelers even dichtbij zijn, return een random speler
            return random.choice([[player_1.rect.center, distance_1], [player_2.rect.center, distance_2]])

    def move_player(self, x, y):
        """ This function moves the player, according to the x and y speeds from the movement function

        :param self: self.ms to control the movement speed
        :param x: movement component in x direction
        :param y: movement component in y direction
        :return: none
        """

        '''If the character is a player, check if it's on the border. If so, make its speed in that direction zero
            If the character is an NPC, we don't need to check the borders, because it will only move toward a 
            player, which can't move outside them'''

        if self.rect.center[0] <= 0 + 0.5 * self.size and x < 0:
            x = 0
        elif self.rect.center[0] >= 800 - 0.5 * self.size and x > 0:
            x = 0
        if self.rect.center[1] <= 0 + 0.5 * self.size and y < 0:
            y = 0
        elif self.rect.center[1] >= 600 - 0.5 * self.size and y > 0:
            y = 0

        ''' If x and y are both 1, make divide both by the square root of 2, so the resultant speed remains 
        the same as when moving straight.'''
        if not(x == 0 and y == 0) :
            if abs(x) == abs(y):
                self.direction = [x / math.sqrt(2), y / math.sqrt(2)]
                self.rect.move_ip(self.direction[0] * self.ms, self.direction[1] * self.ms)
            else:
                self.direction = [x, y]
                self.rect.move_ip(self.direction[0] * self.ms, self.direction[1] * self.ms)

    def player_movement(self, key, rects) -> None:
        """ This function determines the x and y speeds of a player, according to the inputs from the users.

        :param rects1:
        :param rects2:
        :param key:
        """
        # 4 keys pressed
        if key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]]:
            x, y = 0, 0
        # 3 keys pressed
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]]:
            x, y = 0, -1
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[3]]:
            x, y = 0, 1
        elif key[self.controls[0]] * key[self.controls[2]] * key[self.controls[3]]:
            x, y = -1, 0
        elif key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]]:
            x, y = 1, 0
        # 2 keys pressed
        elif key[self.controls[0]] and key[self.controls[2]]:
            x, y = -1, -1
        elif key[self.controls[0]] * key[self.controls[1]]:
            x, y = 0, 0
        elif key[self.controls[0]] * key[self.controls[3]]:
            x, y = -1, 1
        elif key[self.controls[1]] * key[self.controls[2]]:
            x, y = 1, -1
        elif key[self.controls[1]] * key[self.controls[3]]:
            x, y = 1, 1
        elif key[self.controls[2]] * key[self.controls[3]]:
            x, y = 0, 0
        # 1 key pressed
        elif key[self.controls[0]]:
            x, y = -1, 0
        elif key[self.controls[1]]:
            x, y = 1, 0
        elif key[self.controls[2]]:
            x, y = 0, -1
        elif key[self.controls[3]]:
            x, y = 0, 1
        else:
            x, y = 0, 0

        for rect in rects:
            if self.rect.colliderect(rect):
                if (rect[0] >= self.rect.center[0] - 25 and x > 0) or (rect[0] <= self.rect.center[0] - 35 and x < 0):
                    x = 0
                elif (rect[1] >= self.rect.center[1] - 25 and y > 0) or (rect[1] <= self.rect.center[1] - 35 and y < 0):
                    y = 0

        self.move_player(x, y)

    def npc_movement(self, closest, rects) -> None:
        """ This function determines the x and y speed (0 or 1) of an NPC,
        according to the direction to the closest player

        :param closest:
        """
        x, y = 0, 0
        difference = [self.rect.center[0] - closest[0][0], self.rect.center[1] - closest[0][1]]
        distance = closest[1]
        if distance > 0:
            '''We use round to make the NPC movement look like that of the player, having only 8 directions.
            self.rect.move needs didn't seem to work with a float, we also used the round function to turn the 
            floats into integers'''
            x = round(-difference[0] / distance)
            y = round(-difference[1] / distance)

        for rect in rects:
            if self.rect.colliderect(rect):
                if (rect[0] >= self.rect.center[0] - 20 and x > 0) or (rect[0] <= self.rect.center[0] - 40 and x < 0):
                    x = 0
                elif (rect[1] >= self.rect.center[1] - 20 and y > 0) or (rect[1] <= self.rect.center[1] - 40 and y < 0):
                    y = 0

        ''' If x and y are both 1,  divide both by the square root of 2, so the resultant speed remains the same as
        when moving straight.'''
        if abs(x) == abs(y):
            self.rect.move_ip(round(x * self.ms / math.sqrt(2)), round(y * self.ms / math.sqrt(2)))
        else:
            self.rect.move_ip(x * self.ms, y * self.ms)

    def get_gun(self, weapon: object):
        if weapon in self.weapons:
            self.weapons[weapon] += 50
        else:
            weapon = Gun(self, str(weapon))
            self.weapons[weapon] = 50

        self.active_weapon = weapon

    def update_gun(self, key, group):
        return self.active_weapon.update(key, group)



class Gun():
    """The Gun class, creates objects for all gun types. The class can be called to create a gun.
    All Gun's have self.variables like damage, fire speed, ammunition count, bullet speed, knock back.
    And all Gun's will hav functions for ... """

    def __init__(self, Player: object, weapon, color='Yellow', size=5):
        """

        :param Player:
        :param weapon:
        :param color:
        :param size:
        """

        '''Set all the gun specific variables. [damage, fire speed, ammunition, bullet_speed, knock_back]'''
        weapon_variables = {
            'fist':
                {'damage': 2, "fire_speed": 1, 'bullet_speed': 15, 'knockback': 8, 'bullet_count': 0},
            'pistol':
                {'damage': 5, "fire_speed": 30, 'bullet_speed': 15, 'knockback': 3, 'bullet_count': 1},
            'UZI':
                {'damage': 5, "fire_speed": 10, 'bullet_speed': 15, 'knockback': 3, 'bullet_count': 1},
            'shotgun':
                {'damage': 5, "fire_speed": 5, 'bullet_speed': 15, 'knockback': 3, 'bullet_count': 6},
            'Beanbag':
                {'damage': 5, "fire_speed": 5, 'bullet_speed': 15, 'knockback': 3, 'bullet_count': 1},
            'arrow':
                {'damage': 5, "fire_speed": -1, 'bullet_speed': 15, 'knockback': 3, 'bullet_count': 1}}

        self.player = Player

        self.damage = weapon_variables[weapon]['damage']
        self.fire_speed = weapon_variables[weapon]['fire_speed']
        self.bullet_speed = weapon_variables[weapon]['bullet_speed']
        self.bullet_count = weapon_variables[weapon]['bullet_count']
        self.knockback = weapon_variables[weapon]['knockback']

        self.shot_delay = 0

    def update(self, key, group):
        if key[self.player.controls[4]]:
            if self.player.weapons[self] > 0:
                if self.shot_delay == 0:
                    self.shot_delay = self.fire_speed
                    self.player.weapons[self] -= 1
                    bullet = Bullet(self.player.rect.center[0], self.player.rect.center[1], self.player.direction, self.bullet_speed)
                    return group.add(bullet)
            else:
                print('out of ammunition')

        if self.shot_delay > 0:
            self.shot_delay -= 1


        # if key[self.player.controls[4]]:
        #     return Bullet(self.player.rect.center[0], self.player.rect.center[1], self.player.direction, 40)
        # else:
        #     return False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction: list, bullet_speed=10, damage=5, knockback=1):
        """This function creates a bullet with given direction, speed, damage and knockback.

        :param x:
        :param y:
        :param direction:
        :param bullet_speed:
        :param damage:
        :param knockback:
        :return:
        """
        pygame.sprite.Sprite.__init__(self)
        size = round(2 + 0.01 * damage)
        self.size = size
        self.image = pygame.Surface((size, size))
        self.image.fill("Black")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.direction = direction
        self.speed = bullet_speed
        self.knockback = knockback

    def update_bullets(self):
        """This function updates the movement of bullets. And terminates then when they exit the field of vision(the screen).

        :return:
        """
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.rect.move_ip(x, y)

        if self.rect.center[0] <= 0 - self.size:
            self.kill()
        elif self.rect.center[0] >= 800 + self.size:
            self.kill()
        elif self.rect.center[1] <= 0 - self.size:
            self.kill()
        elif self.rect.center[1] >= 600 + self.size:
            self.kill()
