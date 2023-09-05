#!/usr/bin/python3
# convert_to_uppercase.py
def uppercase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        result += uppercase_char

    print("{}".format(result))
