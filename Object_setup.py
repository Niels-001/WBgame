import pygame
import math


class Character(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.ms = 5

    def move(self, x, y):
        if abs(x) == abs(y):
            self.rect.move_ip(x * self.ms, y * self.ms)
        else:
            self.rect.move_ip(x * self.ms * math.sqrt(2), y * self.ms * math.sqrt(2))

    def inputs(self, up, down, left, right):
        key = pygame.key.get_pressed()
        # print(key[pygame.K_a], key[pygame.K_d], key[pygame.K_w], key[pygame.K_s])

        if key[left] * key[down] * key[up] * key[down]:
            self.move(0, 0)
        # 3 keys pressed
        elif key[left] * key[right] * key[up]:
            self.move(0, -1)
        elif key[left] * key[right] * key[down]:
            self.move(0, 1)
        elif key[left] * key[up] * key[down]:
            self.move(-1, 0)
        elif key[right] * key[up] * key[down]:
            self.move(1, 0)
        # 2 keys pressed
        elif key[left] and key[up]:
            self.move(-1, -1)
        elif key[left] * key[right]:
            self.move(0, 0)
        elif key[left] * key[down]:
            self.move(-1, 1)
        elif key[right] * key[up]:
            self.move(1, -1)
        elif key[right] * key[down]:
            self.move(1, 1)
        elif key[up] * key[down]:
            self.move(0, 0)
        # 1 key pressed
        elif key[left]:
            self.move(-1, 0)
        elif key[right]:
            self.move(1, 0)
        elif key[up]:
            self.move(0, -1)
        elif key[down]:
            self.move(0, 1)
