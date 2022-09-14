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

    return ''.join(output_mot)

#print(output_str("bonjour", places_lettre("bonjour", "bonjour")))

def run_game(lst_mots: dict) -> None:
    """Jeu du pendu : Prend en param une liste de mots, choisis un mot aléatoirement, demande a l'utilisateur une lettre
    jusqu'à ce qu'il trouve le mot ou qu'il atteigne son nombre max d'essais

    Args:
        lst_mots (list[str]): _description_
    """

    dict_mots = build_dict(lst_mots)

    print(dict_mots)

    difficulty = int(input("Choisissez une difficulté : 5, 6, 7, 8\n"))

    mot_a_deviner = select_word(dict_mots, difficulty)

    print(mot_a_deviner)

    paris = output_str(mot_a_deviner, places_lettre("", mot_a_deviner))

    mot_actuel = ""
    
    print("Mot a deviner :", mot_a_deviner)
    print("Le paris :", paris, "\n")

    lst_dessin_base = [["|---] "], ["| O "], ["| T "], ["|/ \\"], ["|______"]]
    lst_dessin_progression = [["|---] "], ["|   "], ["|   "], ["|   "], ["|______"]]

    mot_trouve = False
    tries_counter = 0
    lettres_devinees = ""

    while not mot_trouve and tries_counter < 5:

        print(paris)

        lettre_user = input("Choisissez une lettre :\n")

        if lettre_user in lettres_devinees or lettre_user not in mot_a_deviner:

            lst_dessin_progression[tries_counter] = lst_dessin_base[tries_counter]

            for e in lst_dessin_progression:
                print(''.join(e))
            tries_counter += 1

        else:
            lettres_devinees += lettre_user

        paris = output_str(mot_a_deviner, places_lettre(lettres_devinees, mot_a_deviner))

        mot_actuel = paris


        if mot_actuel == mot_a_deviner:
            print("TRUE")
            mot_trouve = True

        

        print(tries_counter, "essais.")
        

    if mot_trouve:
        print("Vous avez trouvé le mot", mot_a_deviner)
    else:
        print("Vous avez perdu, le mot à trouver était", mot_a_deviner)

def build_dict(lst_mots: list[str]) -> dict:

    dictionnaire_mots = {} 

    for mot in lst_mots:
        dictionnaire_mots[len(mot)] = []

    for mot in lst_mots:
        
        dictionnaire_mots[len(mot)].append(mot)

    print(dictionnaire_mots)

    return dictionnaire_mots

def select_word(sorted_word: dict, word_len: int) -> str:
    """_summary_

    Args:
        sorted_word (dict): _description_
        word_len (int): _description_

    Returns:
        str: _description_
    """

    mot_choisi = sorted_word[word_len][random.randint(0, len(sorted_word[word_len]))]

    return mot_choisi


liste_mots = dictionnaire("AtelierL3\Atelier3\mots_pendu.txt")

run_game(liste_mots)