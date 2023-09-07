#!/usr/bin/python3

if __name__ == "__main__":
    """Imprime la somme de 1 et 2."""
    from add_0 import add

    premier_nombre = 1
    deuxieme_nombre = 2
    somme = add(premier_nombre, deuxieme_nombre)
    print("{} + {} = {}".format(premier_nombre, deuxieme_nombre, somme))
