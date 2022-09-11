from exercice1 import val_max
from exercice2 import nb_occurences

ENSEMBLE_J = [6, 5, 6, 8, 4, 2, 1, 5]

def histo(F: list) -> list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """

    h = [0] * (val_max(F) + 1)

    for i in range(len(F) + 1):

        h[i] = nb_occurences(F, i)

    return h

print(histo(ENSEMBLE_J))

