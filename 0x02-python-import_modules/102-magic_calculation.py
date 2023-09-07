#!/usr/bin/python3

def magic_calculation(x, y):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if x < y:
        result = add(x, y)
        for i in range(4, 6):
            result = add(result, i)
        return result

    else:
        return sub(x, y)
