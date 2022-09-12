import random

from exercice2 import dictionnaire

def places_lettre(ch: str, mot: str) -> list[int]:
    """Cherche si le caractère ch est present dans mot et dans ce cas renvoie
    une liste des indices de ch dans mot

    Args:
        ch (str): _description_
        mot (str): _description_

    Returns:
        list[int]: _description_
    """

    liste_indices = []

    """
    if len(ch) == 1:
        
        for i in range(len(mot)):

            if ch == mot[i]:

                liste_indices.append(i)
    """
    for i in range(len(mot)):

        for lettre in ch:

            if lettre == mot[i]:

                liste_indices.append(i)

    return liste_indices

def test_place_lettre():

    print(places_lettre("o", "bonjour"))
    print("Résultat attendu :", [1, 4])

# test_place_lettre()

def output_str(mot: str, lpos: list[int]) -> str:
    """Renvoie une chaine de caractères 

    Args:
        mot (str): _description_
        lpos (list[int]): _description_

    Returns:
        str: _description_
    """

    output_mot = ["_"] * len(mot)

    if lpos:

        for i in lpos:
            output_mot[i] = mot[i]

    return output_mot

#print(output_str("bonjour", places_lettre("bonjour", "bonjour")))

def run_game(lst_mots: list[str]):

    mot_a_deviner = lst_mots[random.randint(0, len(lst_mots) - 1)]

    paris = output_str(mot_a_deviner, places_lettre("", mot_a_deviner))

    print(paris)

    return 

liste_mots = dictionnaire("AtelierL3\Atelier3\mots_pendu.txt")

run_game(liste_mots)