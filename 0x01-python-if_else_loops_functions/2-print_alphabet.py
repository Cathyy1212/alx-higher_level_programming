#!/usr/bin/python3
# print_lowercase_alphabet.py

"""Print the lowercase alphabet without a new line after each letter."""
for ascii_value in range(97, 123):
    print("{}".format(chr(ascii_value)), end="")
