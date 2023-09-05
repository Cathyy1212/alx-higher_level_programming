#!/usr/bin/python3
# print_and_return_last_digit.py
def print_last_digit(number):
    if isinstance(number, int):
        last_digit = abs(number) % 10
        print(last_digit, end="")
        return last_digit
    else:
        raise ValueError("Input must be an integer")

# Testez la fonction avec les exemples
try:
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
except ValueError as e:
    print(e)
