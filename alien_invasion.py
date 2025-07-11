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

class AlienInvasion:
    
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True

    def run_game(self):
        """Game loop"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()