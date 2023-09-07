#!/usr/bin/python3

if __name__ == "__main__":
    """Affiche le nombre d'arguments et la liste des arguments."""
    import sys

    nombre_arguments = len(sys.argv) - 1
    if nombre_arguments == 0:
        print("Aucun argument.")
    elif nombre_arguments == 1:
        print("1 argument :")
    else:
        print("{} arguments :".format(nombre_arguments))
    for i in range(nombre_arguments):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
