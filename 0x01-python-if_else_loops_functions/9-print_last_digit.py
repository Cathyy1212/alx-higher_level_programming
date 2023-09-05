#!/usr/bin/python3
# print_and_return_last_digit.py
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")  # Imprime la dernière chiffre sans nouvelle ligne
    return last_digit  # Retourne la dernière chiffre

# Testez la fonction avec vos exemples
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print()  # Imprime une nouvelle ligne pour le dernier résultat
print(r)  # Imprime la dernière chiffre stockée dans la variable 'r'
