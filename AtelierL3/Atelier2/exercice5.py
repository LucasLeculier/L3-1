def vitrine(nb_emplacements: int, liste_objets: list) -> tuple[list]:
    """_summary_

    Args:
        nb_emplacements (int): _description_
        liste_objets (list): _description_

    Returns:
        tuple[list]: _description_
    """

    liste1 = [] * nb_emplacements
    liste2 = [] * nb_emplacements

    for e in liste_objets:
        if e not in liste1 and e not in liste2:
            if e not in liste1 and len(liste1) < nb_emplacements:
                liste1.append(e)
            if e not in liste2 and len(liste2) < nb_emplacements:
                liste2.append(e)
            


    return (liste1, liste2)

nb_emplacements = 4
l_objets = [1, 2, 2, 3, 4, 5, 5]
print(vitrine(nb_emplacements, l_objets))

