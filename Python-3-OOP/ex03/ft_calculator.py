class calculator:
    """Calculator class for vector-scalar arithmetic."""

    def __init__(self, vec):
        """Initialize the calculator with a vector."""
        self.vector = vec
    
    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector and print the result."""
        self.vector = [nb + object for nb in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar and print the result."""
        self.vector = [nb * object for nb in self.vector]
        print(self.vector)
    
    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector and print the result."""
        self.vector = [nb - object for nb in self.vector]
        print(self.vector)
    
    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar and print the result, handles division by zero."""
        try:
            self.vector = [nb / object for nb in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(f"Error: {e}")