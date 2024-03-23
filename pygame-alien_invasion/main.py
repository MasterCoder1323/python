import sys
import pygame
from settings import settings
from ship import Ship
from bullet import Bullet
from enemies import Enemies
from stats import GameStats

class Game:
    """Main Class to Mannage Game"""
    
    def __init__(self):
        """Initialize the game, and create recources."""
        # Initialize pygame and set up display
        pygame.init()
        
        # Initialize settings
        self.settings = settings()
        
        # Stats
        self.stats = GameStats(self)
        
        self.screen = pygame.display.set_mode(self.settings.screen["size"])
        pygame.display.set_caption('Alien Invasion')
        
        # Initialize ship
        self.ship = Ship(self)
        
        # Initialize bullet group
        self.bullets = pygame.sprite.Group()
        
        # Init fire timeout variables
        self.last_fire_time = -1000
        
        # Font for displaying time
        self.font = pygame.font.SysFont(None, 24)
        
        # Aliens
        self.aliens = pygame.sprite.Group()
        self.enemies = Enemies(self)
        self.enemies._create_fleet()
        
        
        
    def _fire_bullet(self):
        current_time = pygame.time.get_ticks()  # Get current time in milliseconds

        if (current_time - self.last_fire_time)/1000 >= self.settings.fire_timeout:  # Check if 1 second has passed
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.last_fire_time = current_time
    
    def _key_down(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving['right'] = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the right.
            self.ship.moving['left'] = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _key_up(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving['right'] = False
        elif event.key == pygame.K_LEFT:
            # Move the ship to the right.
            self.ship.moving['left'] = False
        
    def _check_events(self):
        """Respond to keypresses and mose events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # run keydown events
                self._key_down(event)
            elif event.type == pygame.KEYUP:
                # run keyup events
                self._key_up(event)
    
    def _display_reload(self):
        # Calculate time to next fire
        current_time = pygame.time.get_ticks()  # Get current time in miliseconds
        time_to_next_fire = max(0, self.settings.fire_timeout-((current_time - self.last_fire_time) / 1000))

        # Convert time to string with one decimal place
        time_text = f"Time to Reload: {time_to_next_fire:.1f}s"

        # Render time text as surface
        time_surface = self.font.render(time_text, True, (0,0,0))  # White text

        # Get screen dimensions
        screen_width, screen_height = self.screen.get_size()

        # Place time text at bottom right corner
        self.screen.blit(time_surface, (screen_width - time_surface.get_width() - 10, screen_height - time_surface.get_height() - 10))
    
    def _display_lives(self):
        time_text = f"Lives: {self.stats.ships_left}"

        # Render time text as surface
        time_surface = self.font.render(time_text, True, (0,0,0))  # White text

        # Get screen dimensions
        screen_width, screen_height = self.screen.get_size()

        # Place time text at bottom right corner
        self.screen.blit(time_surface, (screen_width - time_surface.get_width() - 10, screen_height - time_surface.get_height() - 40))
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship.
            self.enemies._create_fleet()
            self.ship.center_ship()
            
            
        else:
            self.stats.game_active = False
    
    
    def _update_screen(self):
        """Update and display screen."""
        # Set background color
        self.screen.fill(self.settings.screen["bg"])
        
        # Draw & update ship.
        self.ship.update_pos()
        self.ship.blitme()
        
        # Draw and update bullet
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            bullet.draw_bullet()
        
        self.enemies._check_bullet_alien_collisions()
        self.enemies.aliens.draw(self.screen)  
        
        # Display time to reload
        self._display_reload()
        
        # Display Lives
        self._display_lives()
        
        # Display Changes
        pygame.display.flip()
    
    def run(self):
        """Begin Main Game Loop"""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Do other stuff
            if self.stats.game_active:
                self.enemies._update_aliens()
                self._update_screen()
            
if __name__ == '__main__':
    # Create game and then run
    g = Game()
    g.run()
        
