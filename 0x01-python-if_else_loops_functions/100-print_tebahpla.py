#!/usr/bin/python3
# print_reverse_alphabet_alternating_case.py

"""Print the alphabet in reverse order."""
uppercase_flag = False

for ascii_value in range(ord('z'), ord('a') - 1, -1):
    if uppercase_flag:
        print("{}".format(chr(ascii_value).upper()), end="")
    else:
        print("{}".format(chr(ascii_value).lower()), end="")

    uppercase_flag = not uppercase_flag
