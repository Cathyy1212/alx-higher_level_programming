#!/usr/bin/python3

if __name__ == "__main__":
    """Affiche la somme de tous les arguments."""
    import sys

    somme = 0
    for i in range(len(sys.argv) - 1):
        somme += int(sys.argv[i + 1])
    print("{}".format(somme))
