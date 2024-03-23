import subprocess
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired by the ship."""
    
    def __init__(self, game):
        """Create bullet object at current pos"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings.bullet
        
        
        # Create sprite
        self.rect = pygame.Rect(0,0,self.settings['width'],self.settings['height'])
        self.rect.midtop = game.ship.rect.midtop
        
        # Store bullets position
        self.y = float(self.rect.y)
        
    def _update_pos(self):
        """Move the bullet up the screen"""
        self.y -= self.settings["speed"]
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw on the screen"""
        self._update_pos()
        pygame.draw.rect(self.screen, self.settings["color"], self.rect)
        
        
if __name__ == '__main__':
    subprocess.call(['python', 'main.py'])