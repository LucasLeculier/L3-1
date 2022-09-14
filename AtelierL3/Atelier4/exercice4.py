from random import randint

def extrait_de_liste(lst: list, nb_elements: int) -> list:
    """_summary_

    Args:
        lst (list): _description_
        nb_elements (int): _description_

    Returns:
        list: _description_
    """

    liste_extrait = []

    for i in range(0, nb_elements):

        rand_num = randint(0, len(lst) - 1)

        liste_extrait.append(lst[rand_num])

    return liste_extrait


if __name__ == '__main__':

    liste_depart = [0, 1, 7, 8, 10, 23, 2]
    print("Liste de départ :", liste_depart)
    liste_extraits = extrait_de_liste(liste_depart, 5)
    print("La liste extraite :", liste_extraits)
    print("La liste de départ doit etre intacte :", liste_depart)
