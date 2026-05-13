import sys
import pygame
from settings import Settings

class AlienInvasion:
  """Overall class to manage game assets and behavior"""

  def __init__(self):
    """Initilize the game , and create game resourses."""
    pygame.init()

    self.settings = Settings()

    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settins.screen_height))

    pygame.display.set_caption("Alien Invasion")


    def run_game(self):
      """Start the main loop for the game"""
      while True:
        # Watch for keyboard and mout events
        for even in pygame.event.get():
          if even.type == pygame.QUIT:
            sys.exit()

            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
          
          #Make the most recently drawn screen visible
          pygame.display.filp()

if __name__ == '__main__':
  #Make a game instace, and run the game.
  ai = AlienInvasion()
  ai.run_game()