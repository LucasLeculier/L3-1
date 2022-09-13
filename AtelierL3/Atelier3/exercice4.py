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

if __name__ == "__main__":
    
    print(mot_correspond("tarte", "t..t."))
    print(mot_correspond("cheval", "c..v..l"))
    print(mot_correspond("cheval", "c..v.l"))
    