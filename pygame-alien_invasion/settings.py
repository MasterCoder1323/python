import subprocess
debug = False
class settings:
    """Class to store game settings"""
    
    def __init__(self):
        """Initialize settings for alien invasion"""
        # Screen settings
        self.screen = {
            "size":(1200,600),
            "bg": (230,230,230)
        }
        
        self.player_speed = 2
        self.fire_timeout = 0.5
        self.ship_limit = 5
        
        # Alien
        self.alien_speed = 1
        self.fleet_direction = 1
        if debug:
            self.fleet_drop_speed = 50
        else:
            self.fleet_drop_speed = 10
        
        # Bullet Settings
        if debug:
            self.bullet = {
                "speed": 1,
                "width": 310,
                "height": 15,
                "color": (60,60,60)
            }
        else:
            self.bullet = {
                "speed": 1,
                "width": 3,
                "height": 15,
                "color": (60,60,60)
            }
            
if __name__ == '__main__':
    subprocess.call(['python', 'main.py'])
