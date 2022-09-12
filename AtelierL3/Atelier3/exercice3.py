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

    if len(ch) == 1:
        
        for i in range(len(mot)):

            if ch == mot[i]:

                liste_indices.append(i)

    return liste_indices

def test_place_lettre():

    print(places_lettre("a", "tamagochi"))
    print("Résultat attendu :", [1, 3])

#test_place_lettre()

def output_str(mot: str, lpos: list[int]) -> str:
    """Renvoie une chaine de caractères 

    Args:
        mot (str): _description_
        lpos (list[int]): _description_

    Returns:
        str: _description_
    """

    output_mot = []

    if lpos:

        for i in range(len(mot)):

            if i == lpos[i]:
                print(i)

    return output_mot

output_str("bonjour", places_lettre("o", "bonjour"))
