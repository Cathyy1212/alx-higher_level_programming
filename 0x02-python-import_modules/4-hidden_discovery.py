#!/usr/bin/python3

if __name__ == "__main__":
    """Affiche tous les noms définis par le module hidden_4."""
    import hidden_4 as cache_4

    noms = dir(cache_4)
    for nom in noms:
        if nom[:2] != "__":
            print(nom)
