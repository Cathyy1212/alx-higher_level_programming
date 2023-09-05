#!/usr/bin/python3
# print_and_return_last_digit.py
# main_0.py
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-98)
print(r)

r = print_last_digit(98)
print(r + print_last_digit(0))
r = print_last_digit(-98)
print(r + r)

r = print_last_digit(0)
print(r + r)

try:
    print_last_digit("Holberton")
except TypeError as e:
    print(e)

def print_last_digit(number):
    if isinstance(number, int):
        last_digit = abs(number) % 10
        print(last_digit, end="")
        return last_digit
    else:
        raise TypeError("Input must be an integer")
