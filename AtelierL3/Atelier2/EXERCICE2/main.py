from re import I


LA_LISTE = [55, 8, 10, 43, 55, 4, 2, 55]

# 1)

def position(L: list, e: int) -> int:

    ind = -1

    for i in range(len(L)):

        if L[i] == e:
            ind = i

    return ind

def position_2(L: list, e: int) -> int:

    ind = -1
    i = 0

    while True:
        if e == L[i]:
            ind = i
            return ind
        i += 1

#print(position_2(LA_LISTE, 55))

# print(position(LA_LISTE, 4))

# 2)
def nb_occurences(L: list, e: int) -> int:

    compteur = 0

    for i in L:

        print(position(L, e))

        if position(L, e) != -1:
            compteur += 1
    
    return compteur

print(nb_occurences(LA_LISTE, 55))