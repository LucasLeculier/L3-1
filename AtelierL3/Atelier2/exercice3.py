LA_LISTE = [-1, 8, 0, -4, 50, 75, -200, 12, 5, 0, -7]

def separer(L: list) -> list:

    nouvelle_liste = [0] * len(L)

    positifs = []
    negatifs = []
    zeros = []

    for e in L:

        if e < 0:
            negatifs.append(e)
        elif e > 0:
            positifs.append(e)
        else:
            zeros.append(e)

    nouvelle_liste = negatifs + zeros + positifs

    return nouvelle_liste

print(LA_LISTE)
print(separer(LA_LISTE))