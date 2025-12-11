class calculator:
    """A simple calculator for basic vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Computes and prints the dot product of two vectors."""
        v = [nb1 * nb2 for nb1, nb2 in zip(V1, V2)]
        result = sum(v)
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Computes and prints the element-wise addition of two vectors."""
        v = [float(nb1 + nb2) for nb1, nb2 in zip(V1, V2)]
        print(f"Add Vector is: {v}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Computes and prints the element-wise subtraction of two vectors."""
        v = [float(nb1 - nb2) for nb1, nb2 in zip(V1, V2)]
        print(f"Sous Vector is: {v}")
