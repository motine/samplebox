import subprocess

class ShellStuff:
    def __init__(self):
        """Reset sound to default."""
        self.volume = 70 # in percent
        self.set_volume()
        
    def louder(self):
        """Increase volume."""
        print("louder...")
        self.volume = min(100, self.volume + 5)
        self.set_volume()
    
    def quieter(self):
        """Decrease volume."""
        print("quieter...")
        self.volume = max(0, self.volume - 5)
        self.set_volume()
        
    def shutdown(self):
        """Shutdown the pi."""
        subprocess.call(["shutdown", "-h", "0"])
        
    def set_volume(self):
        """Actually set the volume via `amixer`."""
        subprocess.call(["amixer", "set", "PCM", "--", "%d%%" % (self.volume,)])
