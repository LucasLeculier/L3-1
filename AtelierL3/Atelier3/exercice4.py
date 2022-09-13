from exercice2 import mots_n_lettres, dictionnaire

def mot_correspond(mot: str, motif: str) -> bool:
    """Renvoie True si mot correspond à motif sinon False

    Args:
        mot (str): _description_
        motif (str): _description_

    Returns:
        bool: _description_
    """

    does_correspond = False

    if len(mot) == len(motif):

        lettre_est_ok = True

        indice = 0

        while lettre_est_ok and indice < len(motif):

            if motif[indice] != ".":

                if mot[indice] != motif[indice]:
                    print(mot[indice], "!=", motif[indice])

                    lettre_est_ok = False
                    does_correspond = False

            indice += 1
            does_correspond = True
            

    return does_correspond

def presente(lettre: str, mot: str) -> int:
    """Renvoie l'indice de lettre dans mot si présente sinon renvoie -1

    Args:
        lettre (str): _description_
        mot (str): _description_

    Returns:
        int: _description_
    """

    indice = -1

    for i in range(0, len(mot), 1):

        if lettre == mot[i]:
            indice = i

    return indice

def mot_possible(mot: str, lettres: str) -> bool:
    """Renvoie True si mot peut etre composé avec les les lettres individuelles
    contenues dans lettres, sinon renvoie False

    Args:
        mot (str): _description_
        lettres (str): _description_

    Returns:
        bool: _description_
    """

    lettres_actuelles = lettres

    mot_recompose_lst = [""] * len(mot)

    mot_est_possible = False

    if len(mot) < len(lettres):
        
        for lettre in lettres:

            if presente(lettre, mot) >= 0:
                lettres_actuelles.replace(lettre, '', 1)
                mot_recompose_lst[presente(lettre, mot)] = lettre

    if ''.join(mot_recompose_lst) == mot:
        mot_est_possible = True 


    return mot_est_possible
        
def mot_optimaux(dico: list[str], lettres: str) -> list[str]:
    """Renvoie la liste des mots de longueur maximal présents dans la liste de mots dico
    que l'on peut faire avec les lettres présentes dans lettres

    Args:
        dico (list[str]): _description_
        lettres (str): _description_

    Returns:
        list[str]: _description_
    """
    """
    liste_mots_longueur = {}

    for mot in dico:

        if mot_possible(mot, lettres):
            liste_mots_longueur[len(mot)] = []

    for mot in dico:

        if mot_possible(mot, lettres):
            liste_mots_longueur[len(mot)].append(mot)

    liste_mots_longueur = dict(sorted(liste_mots_longueur.items()))

    longueur_max = max(liste_mots_longueur)

    print(liste_mots_longueur)
    """

    dict_mots_longueur = {}

    dict_mots = {}

    for i in range(len(lettres), 1, -1):
        if mots_n_lettres(dico, i):
            dict_mots_longueur[i] = []

    for i in range(len(lettres), 1, -1):
        if mots_n_lettres(dico, i):
            dict_mots_longueur[i].append(mots_n_lettres(dico, i))

    # print(dict_mots_longueur)

    longueur_max = max(dict_mots_longueur)

    # print(longueur_max)

    for key in dict_mots_longueur:
        dict_mots[key] = []

    for key, value in dict_mots_longueur.items():
        print(value)
        
        for mot in value:

            if mot_possible(mot, lettres):
                print(mot)

                dict_mots[key][value].append(mot)

    print(dict_mots)

    




if __name__ == "__main__":
    
    print(mot_correspond("tarte", "t..t."))
    print(mot_correspond("cheval", "c..v..l"))
    print(mot_correspond("cheval", "c..v.l"))

    print()

    print(presente("a", "Barbarossa"))
    print(presente("z", "Barbarossa"))

    print()

    print(mot_possible("lapin", "abilnpq"))
    print(mot_possible("cheval", "abilnpq"))

    print()

    print(mot_optimaux(dictionnaire("AtelierL3\Atelier3\mots_scrabble.txt"), "cheval"))


    