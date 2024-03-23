import pygame

class Ship:
    """A class to manace the ship."""
    
    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        # Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start ship at bottom of screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Set movement
        self.moving = {
            "right": False,
            "left": False
        }
        
        # Import settings
        self.settings = game.settings
        
    def update_pos(self):
        """Update ship position ased on movement flag."""
        if self.moving['right'] and self.rect.x < (self.settings.screen["size"][0]-self.rect.width):
            self.rect.x += self.settings.player_speed
        if self.moving['left'] and self.rect.x > 0:
            self.rect.x -= self.settings.player_speed
        
    def blitme(self):
        # Draw at the bottom of the screen
        self.screen.blit(self.image,self.rect)