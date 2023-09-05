#!/usr/bin/python3
# print_fizzbuzz_sequence.py

def print_fizzbuzz_sequence():
    """Print numbers from 1 to 100 according to the FizzBuzz rules.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of both three and five, print FizzBuzz instead of the number.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
