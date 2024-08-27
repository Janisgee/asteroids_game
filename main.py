import pygame
from constants import *

def main():

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  background_color = (0,0,0)

  while True:
    # Create close window button
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    # Fill the screen with black color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()



if __name__ == "__main__":
    main()

