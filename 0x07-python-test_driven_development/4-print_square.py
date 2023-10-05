#!/usr/bin/python3

# 4-print_square.py

"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square of '#' characters.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(0)
        >>> # (no output, as size is 0)
        >>> print_square(1)
        #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
