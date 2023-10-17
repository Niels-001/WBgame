import pygame
import math
import random

npc_speed = 0.25


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

    def direction_closest_player(self, pl1, pl2):
        """

        :param pl1:
        :param pl2:
        :return:
        """
        diff1 = [pl1.rect.center[0] - self.rect.center[0], pl1.rect.center[1] - self.rect.center[1]]
        diff2 = [pl2.rect.center[0] - self.rect.center[0], pl2.rect.center[1] - self.rect.center[1]]

        dist1 = math.sqrt(diff1[0] ** 2 + diff1[1] ** 2)
        dist2 = math.sqrt(diff2[0] ** 2 + diff2[1] ** 2)

        ''' If player 1 is closer, return the direction from the NPC to that player. If either of the distances is 
            equal to zero, the direction will be zero in both direction, i.e. standing still'''
        if dist1 != 0 and dist2 != 0:
            if dist1 <= dist2:
                return [diff1[0] / dist1, diff1[1] / dist1]
            # If player 2 is closer, return the direction from the NPC to that player
            elif dist2 < dist1:
                return [diff2[0] / dist2, diff2[1] / dist2]
        else:
            return [0, 0]

    """This function moves the character in a Direction with x and y components according to the movement speed
            of the character."""

    def move(self, x, y):

        """
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
            if abs(x) == abs(y):
                self.rect.move_ip(x * self.ms, y * self.ms)
            else:
                self.rect.move_ip(x * self.ms * math.sqrt(2), y * self.ms * math.sqrt(2))
        else:
            self.rect.move_ip(x, y)

    '''This function gives a direction for any character, based on the keys being pressed'''
    def player_movement(self, key) -> None:
        """

        :param self:
        :param key:
        """

        # 4 keys pressed
        if key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]]:
            self.move(0, 0)
        # 3 keys pressed
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]]:
            self.move(0, -1)
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[3]]:
            self.move(0, 1)
        elif key[self.controls[0]] * key[self.controls[2]] * key[self.controls[3]]:
            self.move(-1, 0)
        elif key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]]:
            self.move(1, 0)
        # 2 keys pressed
        elif key[self.controls[0]] and key[self.controls[2]]:
            self.move(-1, -1)
        elif key[self.controls[0]] * key[self.controls[1]]:
            self.move(0, 0)
        elif key[self.controls[0]] * key[self.controls[3]]:
            self.move(-1, 1)
        elif key[self.controls[1]] * key[self.controls[2]]:
            self.move(1, -1)
        elif key[self.controls[1]] * key[self.controls[3]]:
            self.move(1, 1)
        elif key[self.controls[2]] * key[self.controls[3]]:
            self.move(0, 0)
        # 1 key pressed
        elif key[self.controls[0]]:
            self.move(-1, 0)
        elif key[self.controls[1]]:
            self.move(1, 0)
        elif key[self.controls[2]]:
            self.move(0, -1)
        elif key[self.controls[3]]:
            self.move(0, 1)

    def npc_movement(self, d: list):
        self.move(d[0], d[1])
