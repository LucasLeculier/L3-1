from exercice2 import nb_occurences

def vitrine(nb_emplacements: int, liste_objets: list) -> tuple[list]:
    """_summary_

    Args:
        nb_emplacements (int): _description_
        liste_objets (list): _description_

    Returns:
        tuple[list]: _description_
    """

    vitrine1 = [] 
    vitrine2 = []

    for i in range(0, len(liste_objets)):

        compteur = [] * nb_occurences(liste_objets, liste_objets[i])

        print(compteur)

        if 



        


                


    return (vitrine1, vitrine2)

nb_emplacements = 4
l_objets = [1, 2, 2, 3, 4, 5, 5]
print(vitrine(nb_emplacements, l_objets))

