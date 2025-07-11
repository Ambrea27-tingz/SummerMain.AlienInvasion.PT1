

class Settings:
    """A class that overhauls all settings for Alien Invasion."""

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        #frames per second
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
