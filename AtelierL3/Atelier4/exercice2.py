from random import randint

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

    for i in range(0, len(liste_melangee)):

        j = randint(i, len(liste_melangee) - 1)

        liste_melangee[i], liste_melangee[j] = liste_melangee[j], liste_melangee[i]

    return liste_melangee

if __name__ == '__main__':

    lst_triee = [i for i in range(10)]
    print("Liste triée de départ :", lst_triee)
    lst_melangee = melange_liste(lst_triee)
    print("Liste mélangée obtenue :", lst_melangee)
    print("La liste de départ doit etre intacte après appel de melange_liste :", lst_triee)
    print()
    assert lst_triee != lst_melangee


 