#!/usr/bin/python3
# print_alphabet_without_q_and_e.py

"""Print the alphabet in lowercase, excluding the letters 'q' and 'e'."""
for ascii_value in range(97, 123):
    current_letter = chr(ascii_value)
    if current_letter != 'q' and current_letter != 'e':
        print("{}".format(current_letter), end="")
