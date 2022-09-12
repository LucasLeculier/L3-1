import matplotlib.pyplot as plt

from exercice1 import val_max
from exercice2 import nb_occurences

ENSEMBLE_J = [6, 5, 6, 8, 4, 2, 1, 5]
ENSEMBLE_J_INJ = [3, 0, 6, 7, 4, 2, 1, 5]

def histo(F: list) -> list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """

    h = [0] * (val_max(F) + 1)

    for i in range(val_max(F) + 1):
        h[i] = nb_occurences(F, i)

    return h

#print(histo(ENSEMBLE_J))

def est_injective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """

    h = histo(F)

    for e in h:

        if e > 1:
            return False

    return True

F1=[6,5,6,7,4,2,1,5]
# print(est_injective(F1))
F2=[3,0,6,7,4,2,1,5]
# print(est_injective(F2))

def est_surjective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """

    h = histo(F)

    for e in h:

        if e < 1:
            return False

    return True

# print(est_surjective(F1))
# print(est_surjective(F2))

def est_bijective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """

    if est_injective(F) and est_surjective(F):
        return True
    else:
        return False

# print(est_bijective(F1))
# print(est_bijective(F2))


def affiche_histo(F: list) -> None:
    """_summary_

    Args:
        F (list): _description_
    """

    print("\nTEST HISTOGRAMME\n")
    print(f"F={F}\n")
    print("HISTOGRAMME\n")

    h = histo(F)
    maxocc = val_max(h)
    #print(maxocc)

    #print(h, "\n")

    list_lignes = []

    for i in range(0, maxocc):
        ligne = ""
        
        for i in range(len(h)):
            if h[i] > 0:
                h[i] -= 1
                ligne += "   #"
            else:
                ligne += "    "
        list_lignes.append(ligne)

    for item in list_lignes[::-1]:
        print(item)
    
    ligne1 = ""
    ligne2 = ""
    for i in range(len(h)):
        ligne1 += "| --"
        if i < 10:
            ligne2 += f"  {i} "
        else:
            ligne2 += f" {i} "
    
    print(ligne1)
    print(ligne2)



L = [1, 5, 5, 5, 9, 11, 11, 15, 15, 15, 15]
#affiche_histo(L)

def test_histogramme(F: list) -> None:

    h = histo(F)
    print(h)

    plt.hist(h)
    plt.show()

test_histogramme(L)