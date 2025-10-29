import matplotlib.pyplot as plt


class Vector:
    """
    A class to represent a Euclidean vector with magnitude and direction.
    
    - A vector is like an arrow pointing in space.
    - It has *components* (like x, y) that define its direction and length.
    - This class can perform math operations (addition, subtraction, scaling)
      and even draw 2D vectors using matplotlib.
    """

    def __init__(self, *numbers: float) -> None:
        """
        Initialize a Vector with one or more numeric components.

        Parameters
        ----------
        *numbers : float or int
            One or more numbers representing the vector's components.
            Example: Vector(3, 4) means a 2D vector (x=3, y=4).

        Raises
        ------
        TypeError
            If any component is not a number.
        ValueError
            If no components are provided.
        """

        # Validate that each component is a number (int or float)
        for number in numbers:
            if not isinstance(number, (float, int)):
                raise TypeError(f"{number} is not a valid number in a vector")

        # Ensure vector is not empty
        if len(numbers) <= 0:
            raise ValueError("Vector can't be empty")

        # Convert all components to floats (avoids boolean issues like True = 1.0)
        self._numbers = tuple(float(number) for number in numbers)

    # -------------------------------
    #       PROPERTIES
    # -------------------------------
    @property
    def numbers(self) -> tuple:
        """Return the vector's numeric components as a tuple."""
        return self._numbers

    # -------------------------------
    #       ADDITION
    # -------------------------------
    def __add__(self, other: "Vector") -> "Vector":
        """
        Add two vectors together, element by element.

        Example:
            Vector(1, 2) + Vector(3, 4) → Vector(4, 6)
        """
        if self.validate_vectors(other):
            numbers = (a + b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    # -------------------------------
    #       SUBTRACTION
    # -------------------------------
    def __sub__(self, other: "Vector") -> "Vector":
        """
        Subtract one vector from another, element by element.

        Example:
            Vector(3, 4) - Vector(1, 2) → Vector(2, 2)
        """
        if self.validate_vectors(other):
            numbers = (a - b for a, b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    # -------------------------------
    #     SCALAR MULTIPLICATION
    # -------------------------------
    def __mul__(self, value: float) -> "Vector":
        """
        Multiply a vector by a number (scalar).

        Example:
            Vector(1, 2) * 3 → Vector(3, 6)
        """
        print("__mul__ is called")  # For learning/demo purposes
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"The value for multiplication must be int or float, not {type(value)}"
            )
        numbers = (value * a for a in self.numbers)
        return Vector(*numbers)

    def __rmul__(self, value: float) -> "Vector":
        """
        Allow multiplication from the left side (commutative property).

        Example:
            3 * Vector(1, 2) → Vector(3, 6)
        """
        print("__rmul__ is called ...")  # For learning/demo purposes
        return self * value

    # -------------------------------
    #       OTHER SPECIAL METHODS
    # -------------------------------
    def __len__(self) -> int:
        """Enable len(Vector) → returns the number of components."""
        return len(self.numbers)

    def __abs__(self) -> float:
        """
        Return the Euclidean norm (magnitude or length) of the vector.
        
        Formula: √(x² + y² + z² + ...)
        """
        return sum(a**2 for a in self.numbers) ** 0.5

    def __getitem__(self, item: int) -> float:
        """Allow indexing or slicing, e.g. v[0] or v[1:]."""
        return self.numbers[item]

    def __repr__(self) -> str:
        """Developer-friendly representation of the vector."""
        return f"Vector{self.numbers}"

    # -------------------------------
    #       VALIDATION HELPER
    # -------------------------------
    def validate_vectors(self, other: "Vector") -> bool:
        """
        Check that another vector is of the same length before operations.
        
        Raises
        ------
        TypeError
            If `other` is not a Vector or if its length differs.
        """
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("Both must be Vectors and have the same length")
        return True

    # -------------------------------
    #       STATIC METHOD
    # -------------------------------
    @staticmethod
    def is2D(vector: "Vector") -> bool:
        """Check if a vector has exactly two components."""
        return len(vector) == 2

    # -------------------------------
    #       PLOTTING METHOD
    # -------------------------------
    def plot(self, *others: "Vector") -> None:
        """
        Plot this vector (and optionally others) on a 2D coordinate system.

        Parameters
        ----------
        *others : Vector
            Other vectors to plot alongside this one.
        """
        X, Y = [], []  # X and Y components of all vectors

        # Collect 2D vectors only (since this is a 2D plot)
        for vector in tuple(others):
            if Vector.is2D(vector) and Vector.is2D(self):
                X.append(vector[0])
                Y.append(vector[1])

        # Add self (the current vector) at the end
        X.append(self[0])
        Y.append(self[1])

        # Create origin points (0, 0) for each vector
        originX = originY = tuple(0 for _ in range(len(X)))

        # Create a new plot
        _, ax = plt.subplots(1)
        ax.quiver(originX, originY, X, Y, scale=1, scale_units="xy", angles="xy")
        ax.set(
            xlabel="x",
            ylabel="y",
            title=f"{self}, {others}",
            xlim=(-2, 10),
            ylim=(-2, 10),
        )
        ax.grid()

        # TODO: Make the xlim and ylim adjust automatically
        # TODO: Clean up title formatting
