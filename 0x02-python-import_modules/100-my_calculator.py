#!/usr/bin/python3

if __name__ == "__main__":
    """Gère les opérations arithmétiques de base."""
    from calculator_1 import add, sub, mul, div 
    import sys

    if len(sys.argv) - 1 != 3:
        print("Utilisation : ./100-my_calculator.py <a> <opérateur> <b>")
        sys.exit(1)

    opérations = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(opérations.keys()):
        print("Opérateur inconnu. Opérateurs disponibles : +, -, * et /")
        sys.exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[3])
    print("{} {} {} = {}".format(x, sys.argv[2], y, opérations[sys.argv[2]](x, y)))
