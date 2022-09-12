from math import floor

LA_LISTE = [55, 8, 10, 43, 55, 4, 2, 55]
LA_LISTE_TRIEE = [1, 5, 7, 10, 33, 165]
LA_LISTE_TRIEE_2 = [0, 5, 8, 9, 22, 67, 80, 81, 107]

# 1)

def position(L: list, e: int) -> int:
    """Renvoie l'index de la position de e dans la liste L

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """

    ind = -1

    for i in range(len(L)):

        if L[i] == e:
            ind = i

    return ind

def position_2(L: list, e: int) -> int:
    """Renvoie l'index de la position de e dans la liste L

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """

    ind = -1
    i = 0

    while True:
        if e == L[i]:
            ind = i
            return ind
        i += 1

# print(position_2(LA_LISTE, 55))

# print(position(LA_LISTE, 4))

# 2)
def nb_occurences(la_liste: list, e: int) -> int:
    """Renvoie le nombre d'occurences de e dans la liste la_liste

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """

    compteur = 0

    for i in la_liste:
        if e == i:
            compteur += 1
    
    return compteur

# print(nb_occurences(LA_LISTE, 55))

def est_triee_for(L: list) -> bool:
    """Renvoie True si la liste L est triée sinon renvoie False

    Args:
        L (list): _description_

    Returns:
        bool: _description_
    """
    actuel = L[0]
    est_triee = True

    for i in range(len(L) - 1):

        if actuel <= L[i+1]:
            actuel = L[i+1]
        else:
            est_triee = False

    return est_triee

# print(est_triee_for(LA_LISTE))
# print(est_triee_for(LA_LISTE_TRIEE))

def est_triee_while(L: list) -> bool:
    """Renvoie True si la liste L est triée sinon renvoie False

    Args:
        L (list): _description_

    Returns:
        bool: _description_
    """

    actuel = L[0]
    i = 0
    est_triee = True
    counter = 0

    while est_triee and i < len(L) - 1:
        counter += 1

        if actuel <= L[i+1]:
            actuel = L[i+1]
        else:
            est_triee = False

        i += 1
    #print(counter)
    return est_triee

#print(est_triee_while(LA_LISTE))
#print(est_triee_while(LA_LISTE_TRIEE))
#print(est_triee_while(LA_LISTE_TRIEE_2))

def position_tri(L: list, e: int) -> int:
    """Renvoie l'index de e dans la liste L supposée triée

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    l_trie = sorted(L)

    debut_liste = 0
    fin_liste = len(L) - 1

    a_trouve = False

    index_trouve = 0

    while not a_trouve and debut_liste <= fin_liste:
        millieu_liste = floor((debut_liste + fin_liste) / 2)
        index_trouve = millieu_liste
        
        if l_trie[millieu_liste] == e:
            a_trouve = True
        else:
            if e > l_trie[millieu_liste]:
                debut_liste = millieu_liste + 1
            else:
                fin_liste = millieu_liste - 1

    return index_trouve

# print(position_tri(LA_LISTE_TRIEE_2, 80))

def a_repetitions(L: list) -> bool:
    """Renvoie True si la liste L contient des répétitions sinon False

    Args:
        L (list): _description_

    Returns:
        bool: _description_
    """
    t = []

    for e in L:
            
        if e in t:
            return True
        else:
            t.append(e)
        
    return False

#LA_LISTE_REPET = [6, 5, 7, 10, 8, 11]
#print(a_repetitions(LA_LISTE_REPET))
