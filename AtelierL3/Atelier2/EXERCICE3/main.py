LA_LISTE = [-1, 8, -4, 50, 75, -200, 12, 5, -7]

def separer(L: list) -> list:

    nouvelle_liste = [0] * len(L)

    actuel_positif = len(L) - 1
    actuel_negatif = 0

    for e in L:

        if e < 0:
            nouvelle_liste[actuel_negatif] = e
            actuel_negatif += 1
        else:
            nouvelle_liste[actuel_positif] = e
            actuel_positif -= 1

    return nouvelle_liste

print(LA_LISTE)
print(separer(LA_LISTE))