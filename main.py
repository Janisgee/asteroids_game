import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  # Restrict game draw 60FPS
  clock = pygame.time.Clock()
  # Group for empty group - all objects can be updated
  updatable_gp = pygame.sprite.Group()
  # Group for all objects can be drawn
  drawable_gp = pygame.sprite.Group()
  # Group for all objects of asteroids
  asteroids_gp = pygame.sprite.Group()
  # Group for bullets
  shot_gp = pygame.sprite.Group()

  # Add player to update and draw group
  Player.containers = (updatable_gp, drawable_gp)
  # Add asteroids to update and draw group
  Asteroid.containers = (updatable_gp, drawable_gp, asteroids_gp)
  # Add asteroidfield to update group
  AsteroidField.containers = (updatable_gp)
  # Add bullets to update group
  Shot.containers = (updatable_gp, drawable_gp, shot_gp)


  background_color = (0,0,0)
  x = SCREEN_WIDTH/2
  y = SCREEN_HEIGHT/2
  # Create Object
  player = Player(x,y)
  asteroidfield = AsteroidField()

  dt = 0


  while True:
    # Create close window button
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # Update
    for obj in updatable_gp:
      obj.update(dt)
    
    # Collide check
    for obj in asteroids_gp:
      for shot in shot_gp:
        if obj.check_collision(shot):
          #.kill() method is build-in pygame
          obj.split()
          shot.kill()
      if obj.check_collision(player):
        print("Game over!")
        return
    

    # Fill the screen with black color
    screen.fill(background_color)

    # Draw 
    for obj in drawable_gp:
      obj.draw(screen)

    # Update the display
    pygame.display.flip()

    # Pause game loop until 1/60 second has pass
    # Time passed how many second
    dt = clock.tick(60) / 1000
    




if __name__ == "__main__":
    main()

