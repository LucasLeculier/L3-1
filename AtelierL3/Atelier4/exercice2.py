def melange_liste(lst: list) -> list:
    """Renvoie une liste issue du mélange de la liste
    passée en paramètre, la liste passée en paramètre doit
    etre intacte à la sortie de la fonction

    Args:
        lst (list): _description_

    Returns:
        list: _description_
    """

    liste_melangee = [e for e in lst]

    return liste_melangee

if __name__ == '__main__':

    la_liste = [1, 2]
    print(melange_liste(la_liste))
    print(la_liste)

 