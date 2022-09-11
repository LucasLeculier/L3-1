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


# def affiche_histo(F: list) -> :