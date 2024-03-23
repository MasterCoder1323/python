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
        
        # Bullet Settings
        self.bullet = {
            "speed": 1,
            "width": 3,
            "height": 15,
            "color": (60,60,60)
        }
