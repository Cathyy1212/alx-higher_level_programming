#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, side_length=0):
        """Initialize a new square.

        Args:
            side_length (int): The side length of the new square.
        """
        self.side_length = side_length

    @property
    def side_length(self):
        """Get/set the current side length of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        elif value < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = value

    def area(self):
        """Return the current area of the square."""
        return self.__side_length * self.__side_length

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()
