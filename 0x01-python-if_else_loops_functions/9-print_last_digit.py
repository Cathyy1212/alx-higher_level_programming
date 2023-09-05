#!/usr/bin/python3
# print_and_return_last_digit.py
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

# Testez la fonction avec les exemples
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
