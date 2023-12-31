#!/usr/bin/python3

# 0-add_integer.py
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)

