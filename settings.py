

class Settings:
    """A class that overhauls all settings for Alien Invasion."""

    def __init__(self):
        """Prepare the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        #baby blue background
        self.bg_color = (65, 131, 215)

         # Ship settings
        self.ship_speed = 1.7

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 13
        self.bullet_color = (255, 255, 255) 
        self.bullets_allowed = 3   