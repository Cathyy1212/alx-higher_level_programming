#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(parameter_a, parameter_b, parameter_c):
    """Match bytecode provided by Holberton School."""
    if parameter_a < parameter_b:
        return parameter_c
    if parameter_c > parameter_b:
        return parameter_a + parameter_b
