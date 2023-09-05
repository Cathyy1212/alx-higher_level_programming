#!/usr/bin/python3
# is_lowercase_character.py

def is_lowercase(c):
    """Check if the character is lowercase."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
