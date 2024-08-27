import pygame
from player import Player
from constants import *

def main():

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  background_color = (0,0,0)
  x = SCREEN_WIDTH/2
  y = SCREEN_HEIGHT/2
  # Create player
  player = Player(x,y)

  # Restrict game draw 60FPS
  clock = pygame.time.Clock()
  dt = 0

  while True:
    # Create close window button
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # Fill the screen with black color
    screen.fill(background_color)

    # Draw player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Pause game loop until 1/60 second has pass
    clock.tick(60)
    # Time passed how many second
    dt = clock.get_time()/1000
    # print(dt)



if __name__ == "__main__":
    main()

