from random import randint

def element_de_liste(lst: list) -> list:
    """_summary_

    Args:
        lst (list): _description_
        nb_elements (int): _description_

    Returns:
        list: _description_
    """

    return lst[randint(0, len(lst) - 1)]


if __name__ == '__main__':

    liste_base = [0, 1, 2, 3, 10, 5, 15]
    print(element_de_liste(liste_base))