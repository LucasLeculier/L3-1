from random import *

def gen_liste_random_int(taille: int=10, int_binf: int=0, int_bsup: int=10) -> list[int]:
    """Génère une liste d'entiers aléatoire entre int_binf et int_bsup, par
    défaut entre 0 et 10

    Args:
        int_binf (int, optional): _description_. Defaults to 0.
        int_bsup (int, optional): _description_. Defaults to 10.

    Returns:
        list[int]: _description_
    """

    return [randint(int_binf, int_bsup - 1) for i in range(taille)]

def melange_liste(lst: list) -> list:
    """Renvoie une liste issue du mélange de la liste
    passée en paramètre

    Args:
        lst (list): _description_

    Returns:
        list: _description_
    """

    

if __name__ == '__main__':

    print(gen_liste_random_int())
    print(gen_liste_random_int(4, 10, 15))
    print()