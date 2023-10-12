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
      self.rect.move_ip(x*self.ms * math.sqrt(2), y*self.ms * math.sqrt(2))