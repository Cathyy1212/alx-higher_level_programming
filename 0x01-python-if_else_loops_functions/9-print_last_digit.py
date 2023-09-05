#!/usr/bin/python3
# print_and_return_last_digit.py

def print_and_return_last_digit(input_number):
    """Print the last digit of a number and return it."""
    last_digit = abs(input_number) % 10
    print(last_digit, end="")
    return last_digit
