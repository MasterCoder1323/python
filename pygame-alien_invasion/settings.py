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
