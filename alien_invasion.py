""" 
alien_invasion.py

Title: Alien Invasion

Discription: Alien Invasion is a creative game where the player controls a spaceship
and tries to annihilate neigboring enemies by shooting down the invading aliens. 
The game is built using Pygame.

Author: Ambrea Williams

Date: 2025-07-11
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
        """Main class that manages the game assets and behavior.""" 

        def __init__(self):
                    """Prepare the game, and create game resources."""
                    pygame.init()
                    self.clock = pygame.time.Clock()
                    self.settings = Settings()
                    #Small screen mode
                    self.screen = pygame.display.set_mode((1200, 800))
                    self.settings.screen_width = self.screen.get_rect().width
                    self.settings.screen_height = self.screen.get_rect().height

                    pygame.display.set_caption("Alien Invasion")
                    
                    self.ship = Ship(self)
                    self.bullets = pygame.sprite.Group()

                    #background color.
                    self.bg_color = self.settings.bg_color
                    self.game_active = False

        def run_game(self):
        #Game loop
         while self.running:
            self._check_events()       
            
            self._update_screen()
            self.clock.tick(self.settings.FPS)

        def _update_screen(self):
         self.screen.blit(self.bg, (0, 0)) 
         self.ship.draw()   
        pygame.display.flip()

        def _check_events(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
        
                
if __name__ == '__main__':
    # Set up a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()



        
        








