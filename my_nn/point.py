class Point:
    """Basic point representation."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._nn = None
        self._nn_distance = None

    def __str__(self):
        """Creates a string representation of the point."""
        return f"({self.x}, {self.y})"

    def as_tup(self):
        return self.x, self.y

    @property
    def nearest_neighbor(self):
        """Accessor method: if set, returns the points nearest neighbor."""
        return self._nn

    @nearest_neighbor.setter
    def nearest_neighbor(self, value):
        """Accessor method: sets the nearest neighboring point."""
        if not value:
            raise ValueError(f"Must give a value to set: value: {value}")
        if not type(self) == type(value):
            # TODO ugly, but not sure how else to do this
            raise TypeError(f"Nearest neighbor must be of type Point: {type(value)}")
        self._nn = value

    @property
    def distance_to_nearest_neighbor(self):
        """Accessor method: if set, returns the distance to nearest neighbor"""
        return self._nn_distance

    @distance_to_nearest_neighbor.setter
    def distance_to_nearest_neighbor(self, value: float):
        """Accessor method: sets the distance to nearest neighbor."""
        if not value:
            raise ValueError(f"Must give a value to set: value: {value}")
        self._nn_distance = value
