
# Liste a tester
LA_LISTE = [10, 4, 6, 8, 1, 6, 2]

def somme_for(L: list) -> float:

    somme = 0

    for i in range(len(L)):
        somme += L[i]
    
    return somme


def somme_foreach(L: list) -> int:

    somme = 0

    for n in L:
        somme += n
    
    return somme

#print(somme_foreach(LA_LISTE))

def somme_while(L: list) -> float:

    i = 0
    somme = 0

    while i < len(L):
        somme += L[i]
        i += 1
    
    return somme


def test_somme():

    print("Somme avec le for :", somme_for(LA_LISTE))
    print("Somme avec le foreach :", somme_foreach(LA_LISTE))
    print("Somme avec le while :", somme_while(LA_LISTE))

#test_somme()

def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme_while([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme_while(S))

#test_exercice1()

# 3)

def moyenne(L: list) -> float:
    """Renvoie la moyenne des éléments de la liste L

    Args:
        L (list): Liste d'entiers 

    Returns:
        float: La moyenne des éléments de L
    """

    somme = somme_foreach(L)

    if L:
        return somme / len(L)
    else:
        return 0

# print(moyenne(LA_LISTE))
# print(moyenne([]))
# help(moyenne)

# 4)

def nb_sup(L: list, e: int) -> int:

    compteur = 0

    for i in L:
        if e < i:
            compteur += 1
    
    return compteur

#print(nb_sup(LA_LISTE, 5))

# 5) 

def moy_sup(L: list, e: int) -> int:

    compteur = 0
    total = []

    if len(L) > 0:
        for i in L:
            if e < i:
                compteur += 1
                total.append(i)
        return moyenne(total)
    else:
        return 0

# print(moy_sup(LA_LISTE, 5)) 
# print(moy_sup([], 5))

# 6)

def val_max(L: list) -> float:

    le_max = L[0]

    for e in L:
        if le_max < e:
            le_max = e

    return le_max

#print(val_max(LA_LISTE))

# 7)

def ind_max(L: list) -> float:

    le_max = L[0]

    i_max = 0

    for i in range(len(L)):
        if le_max < L[i]:
            le_max = L[i]
            i_max = i

    return i_max        


#print(ind_max(LA_LISTE))

