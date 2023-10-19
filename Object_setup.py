import pygame
import math
import random
import typing


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
            self.controls = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
            self.ms = 5
        elif player == 2:
            self.player = True
            self.controls = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
            self.ms = 5
        else:
            self.player = False
            x = random.randint(50, 750)
            y = random.randint(50, 550)
            self.ms = 1

        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.Surface((size, size))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    """ This function checks which player is closer to the NPC being checked and then returns the direction
        for that NPC to move in """

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
        else:   # Als beide spelers even dichtbij zijn, return een random speler
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
        if self.player:
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
            if abs(x) == abs(y):
                self.rect.move_ip(x * self.ms / math.sqrt(2), y * self.ms / math.sqrt(2))
            else:
                self.rect.move_ip(x * self.ms, y * self.ms)
        else:
            self.rect.move_ip(x * self.ms, y * self.ms)

    def player_movement(self, key) -> None:
        """ This function determines the x and y speeds of a player, according to the inputs from the users.

        :param key:
0        """
        # 4 keys pressed
        if key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]]:
            self.move_player(0, 0)
        # 3 keys pressed
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]]:
            self.move_player(0, -1)
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[3]]:
            self.move_player(0, 1)
        elif key[self.controls[0]] * key[self.controls[2]] * key[self.controls[3]]:
            self.move_player(-1, 0)
        elif key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]]:
            self.move_player(1, 0)
        # 2 keys pressed
        elif key[self.controls[0]] and key[self.controls[2]]:
            self.move_player(-1, -1)
        elif key[self.controls[0]] * key[self.controls[1]]:
            self.move_player(0, 0)
        elif key[self.controls[0]] * key[self.controls[3]]:
            self.move_player(-1, 1)
        elif key[self.controls[1]] * key[self.controls[2]]:
            self.move_player(1, -1)
        elif key[self.controls[1]] * key[self.controls[3]]:
            self.move_player(1, 1)
        elif key[self.controls[2]] * key[self.controls[3]]:
            self.move_player(0, 0)
        # 1 key pressed
        elif key[self.controls[0]]:
            self.move_player(-1, 0)
        elif key[self.controls[1]]:
            self.move_player(1, 0)
        elif key[self.controls[2]]:
            self.move_player(0, -1)
        elif key[self.controls[3]]:
            self.move_player(0, 1)

    def npc_movement(self, closest) -> None:
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

        ''' If x and y are both 1,  divide both by the square root of 2, so the resultant speed remains the same as
        when moving straight.'''
        if abs(x) == abs(y):
            self.rect.move_ip(x * self.ms / math.sqrt(2), y * self.ms / math.sqrt(2))
        else:
            self.rect.move_ip(x * self.ms, y * self.ms)
