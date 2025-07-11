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
                    """Start the main loop for the game."""
                    while True:
                            self._check_events()
                            self.ship.update()
                            self._update_bullets()
                            self._update_screen()
                            self.clock.tick(60)

        def _update_bullets(self):
            """Update the position of bullets and remove old bullets."""
            self.bullets.update()
                               
                                
                
        #Get remove bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                     self.bullets.remove(bullet)
                #print(len(self.bullets))  

                  
        def _check_events(self):
             """React to keypresses and mouse events."""               
             for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                        sys.exit()
                            
                   elif event.type == pygame.KEYDOWN:
                          self._check_keydown_events(event)
        
                   elif event.type == pygame.KEYUP:
                          self._check_keyup_events(event) 
        
        def _check_keydown_events(self, event):
                    """React to keypresses."""                 
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_q:
                     sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()         
                        
        def _check_keyup_events(self, event):
                    """React to key releases."""            
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_q:
                        sys.exit()  

        def _fire_bullet(self):
            """Generate a new bullet and add it to the bullets group."""
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)                
        
        def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""                    
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            for bullet in self.bullets.sprites():
             bullet.draw_bullet()
            self.ship.blitme()
            
            pygame.display.flip()   
            
        
                
if __name__ == '__main__':
    # Set up a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()



        
        








