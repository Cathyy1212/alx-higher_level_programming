que(x, y):
    resultat = 0
    for i in range(1, 3):
        try:
            if i > x:
                raise Exception('Trop loin')
            else:
                resultat += x ** y / i
        except:
            resultat = y + x
            break
    return (resultat)
