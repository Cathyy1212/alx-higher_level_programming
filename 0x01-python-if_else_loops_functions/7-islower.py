#!/usr/bin/python3
# is_lowercase_character.
def islower(c):
    # Check if the ASCII value of the character is in the lowercase range (97 to 122)
    return ord(c) >= 97 and ord(c) <= 122

