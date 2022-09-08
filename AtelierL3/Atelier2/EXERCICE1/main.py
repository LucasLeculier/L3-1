
# Liste a tester
LA_LISTE = [0, 4, 6, 8, 1, 6]

def somme_for(L: list) -> float:

    somme = 0

    for i in range(len(L)):
        somme += L[i]
    
    return somme




def somme_foreach(L: list) -> float:

    somme = 0

    for n in L:
        somme += n
    
    return somme




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

test_somme()