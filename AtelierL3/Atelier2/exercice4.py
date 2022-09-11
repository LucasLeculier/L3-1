from exercice1 import val_max
from exercice2 import nb_occurences

ENSEMBLE_J = [6, 5, 8, 4, 2, 1, 5, 10]

def histo(F: list) -> list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """

    h = [0] * val_max(F)

    for i in range(len(F)):

        h[i] = nb_occurences(F, F[i])

    return h

print(histo(ENSEMBLE_J))

