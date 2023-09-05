#!/usr/bin/python3
# print_decimal_and_hexadecimal.py

"""Print numbers from 0 to 98 in both decimal and hexadecimal."""
for decimal_number in range(0, 99):
    hexadecimal_number = hex(decimal_number)
    print("{} = {}".format(decimal_number, hexadecimal_number))
