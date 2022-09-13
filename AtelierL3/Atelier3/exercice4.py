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


    