import pygame
import math
import random


class Character(pygame.sprite.Sprite):
    def __init__(self, col, x = random.randint(50, 750), y = random.randint(50, 550), player = 0 , size = 30):
        """

        :param col:
        :param x:
        :param y:
        :param player:
        """
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.Surface((size, size))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.ms = 5
        if player == 1:
          self.controls = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
        elif player == 2:
          self.controls = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        elif player == 0:
            self.controls = list()

    def move(self, x, y):
        """This function moves the character in a Direction with x and y components according to the movement speed of the character.

          :param self: self.ms to control the movement speed
          :param x: movement component in x direction
          :param y: movement component in y direction
          :return: none
          """
        if self.rect.center[0] <= 0 + 0.5 * self.size and x < 0 :
            x = 0
        elif self. rect.center[0] >= 800 - 0.5 * self.size and x > 0:
            x = 0
        if self.rect.center[1] <= 0 + 0.5 * self.size and y < 0:
            y = 0
        elif self. rect.center[1] >= 600 - 0.5 * self.size and y > 0:
            y = 0
        if abs(x) == abs(y):
          self.rect.move_ip(x * self.ms, y * self.ms)
        else:
          self.rect.move_ip(x*self.ms * math.sqrt(2), y*self.ms * math.sqrt(2))
    def update_move(self, key) -> None:
        """

          :param self:
          :param key:
          """
          #4 keys pressed
        if key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]] :
            self.move(0,0)
        # 3 keys pressed
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[2]] :
            self.move(0,-1)
        elif key[self.controls[0]] * key[self.controls[1]] * key[self.controls[3]] :
            self.move(0, 1)
        elif key[self.controls[0]] * key[self.controls[2]] * key[self.controls[3]] :
            self.move(-1, 0)
        elif key[self.controls[1]] * key[self.controls[2]] * key[self.controls[3]] :
            self.move(1, 0)
        # 2 keys pressed
        elif key[self.controls[0]] and key[self.controls[2]]:
            self.move(-1, -1)
        elif key[self.controls[0]] * key[self.controls[1]] :
            self.move(0, 0)
        elif key[self.controls[0]] * key[self.controls[3]] :
            self.move(-1, 1)
        elif key[self.controls[1]] * key[self.controls[2]] :
            self.move(1, -1)
        elif key[self.controls[1]] * key[self.controls[3]] :
            self.move(1, 1)
        elif key[self.controls[2]] * key[self.controls[3]] :
            self.move(0, 0)
        # 1 key pressed
        elif key[self.controls[0]] :
            self.move(-1, 0)
        elif key[self.controls[1]] :
            self.move(1, 0)
        elif key[self.controls[2]] :
            self.move(0, -1)
        elif key[self.controls[3]]:
            self.move(0, 1)