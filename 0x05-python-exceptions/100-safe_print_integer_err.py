#!/usr/bin/python3

import sys

def imprimer_entier_en_securite_avec_erreurs(valeur):
    """Affiche un entier avec "{:d}".format().

    Si une erreur de valeur est attrapée, un message correspondant
    est imprimé sur la sortie d'erreur standard.

    Args:
        valeur (int): L'entier à afficher.

    Returns:
        Si une TypeError ou ValueError se produit - False.
        Sinon - True.
    """
    try:
        print("{:d}".format(valeur))
        return True
    except (TypeError, ValueError):
        print("Exception : {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
