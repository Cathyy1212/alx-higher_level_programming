#!/usr/bin/python3
# print_and_return_last_digit.py
def print_last_digit(number):
    if isinstance(number, int):
        last_digit = abs(number) % 10
        print(last_digit, end="")
        return last_digit
    else:
        raise ValueError("Input must be an integer")
