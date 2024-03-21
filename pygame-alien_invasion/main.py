import sys
import pygame
from settings import settings
from ship import Ship

class Game:
    """Main Class to Mannage Game"""
    
    def __init__(self):
        """Initialize the game, and create recources."""
        # Initialize pygame and set up display
        pygame.init()
        
        # Initialize settings
        self.settings = settings()
        
        self.screen = pygame.display.set_mode(self.settings.screen["size"])
        pygame.display.set_caption('Alien Invasion')
        
        # Initialize ship
        self.ship = Ship(self)
        
        
        
    def _check_events(self):
        """Respond to keypresses and mose events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.moving['right'] = True
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the right.
                    self.ship.moving['left'] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.moving['right'] = False
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the right.
                    self.ship.moving['left'] = False
    
    def _update_screen(self):
        """Update and display screen."""
        # Set background color
        self.screen.fill(self.settings.screen["bg"])
        
        # Draw & update ship.
        self.ship.update_pos()
        self.ship.blitme()
        
        # Display Changes
        pygame.display.flip()
    
    def run(self):
        """Begin Main Game Loop"""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
                    
            # Update the Screen
            self._update_screen()
            
if __name__ == '__main__':
    # Create game and then run
    g = Game()
    g.run()
        
