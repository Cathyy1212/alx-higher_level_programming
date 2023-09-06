#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(input_str, position):
    """Create a copy of the string."""
    if position < 0:
        return input_str
    return input_str[:position] + input_str[position + 1:]
