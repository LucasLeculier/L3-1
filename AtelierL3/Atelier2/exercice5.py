from exercice4 import histo
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

    h = histo(liste_objets)

    # print("Liste objets :", liste_objets)
    # print("histogramme :", h)

    taille_lst_objets = len(liste_objets)

    if taille_lst_objets <= nb_emplacements * 2:

        for i in range(0, len(h)):

            if h[i] == 2:
                vitrine1.append(i)
                vitrine2.append(i)

        for i in range(0, len(h)):
            
            if h[i] == 1:

                if len(vitrine1) < nb_emplacements:

                    vitrine1.append(i)
                
                elif len(vitrine2) < nb_emplacements:

                    vitrine2.append(i)

        # print("Vitrine 1 :", vitrine1)
        # print("Vitrine 2 :", vitrine2)

    if (len(vitrine1) + len(vitrine2)) < len(liste_objets):
        vitrine1 = []
        vitrine2 = []

    return (vitrine1, vitrine2)

if __name__ == '__main__':

    print(vitrine(4, [1, 2, 2, 3, 4, 5, 5])) # ([1, 2, 3, 5], [2, 4, 5])
    print()
    print(vitrine(5, [1, 1, 2, 3, 4, 4, 5, 8, 10])) # ([1, 2, 3, 4, 5], [1, 2, 4, 5, 8, 10])
    print()
    print(vitrine(2, [1, 1, 1, 4])) # ([], [])
    print()
    print(vitrine(3, [1, 1, 2, 4, 5, 7, 8])) # ([], [])

