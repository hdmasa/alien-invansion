import sys
import pygame

class AlienInvasion:
  """Overall class to manage game assets and behavior"""

  def __init__(self):
    """Initilize the game , and create game resourses."""
    pygame.init()

    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #Set the background color
    self.bg_color = (230, 230, 230)

    def run_game(self):
      """Start the main loop for the game"""
      while True:
        # Watch for keyboard and mout events
        for even in pygame.event.get():
          if even.type == pygame.QUIT:
            sys.exit()

            #redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
          
          #Make the most recently drawn screen visible
          pygame.display.filp()

if __name__ == '__main__':
  #Make a game instace, and run the game.
  ai = AlienInvasion()
  ai.run_game()