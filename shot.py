import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
  def __init__(self, x,y, radius):
    super().__init__(x,y,SHOT_RADIUS)


  def draw(self, screen):
    color = (255, 255, 255)
    line_width = 2
    pygame.draw.circle(screen, color, self.position, self.radius, line_width)
  
  def update(self, dt):
    self.position += self.velocity * dt