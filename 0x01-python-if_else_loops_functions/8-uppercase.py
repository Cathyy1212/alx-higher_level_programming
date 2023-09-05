#!/usr/bin/python3
# convert_to_uppercase.py
def uppercase(input_str):
    for char in input_str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char  # If not lowercase, keep it as is
        print(uppercase_char, end="")
    print()  # Print a new line after the loop


