#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, side_length=0):
        """Initialize a new Square.

        Args:
            side_length (int): The length of a side of the new square.
        """
        if not isinstance(side_length, int):
            raise TypeError("side_length must be an integer")
        elif side_length < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = side_length
