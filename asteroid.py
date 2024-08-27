import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid (CircleShape):
  def __init__ (self,x, y, radius):
    super().__init__(x, y, radius)
    self.position = pygame.Vector2(x, y)
    self.radius = radius

  def draw(self, screen):
    color = (255, 255, 255)
    line_width = 2
    pygame.draw.circle(screen, color, self.position, self.radius, line_width)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
       return

    # From 20 to 50 degree
    random_angle = random.uniform(20,50)
    new_radius = self.radius - ASTEROID_MIN_RADIUS 

    a = self.velocity.rotate(random_angle)
    b = self.velocity.rotate(-random_angle)

    new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)

    new_asteroid_1.velocity = a * 1.2

    new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

    new_asteroid_2.velocity = b * 1.2




   
