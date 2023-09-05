#!/usr/bin/python3
# convert_to_uppercase.py

def convert_to_uppercase(input_str):
    """Convert a string to uppercase."""
    for char in input_str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
