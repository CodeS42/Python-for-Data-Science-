from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing the king using multiple inheritance."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the king with inherited Baratheon traits."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Set the king's eye color."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the king's hair color."""
        self.hairs = color

    def get_eyes(self):
        """Return the king's eye color."""
        return self.eyes

    def get_hairs(self):
        """Return the king's hair color."""
        return self.hairs
