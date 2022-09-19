import exercice1
from exercice2 import melange_liste
import exercice3
import exercice4

import random

import time

def generer_liste(taille: int, ordre: str) -> list[int]:
    """Génère une liste

    Args:
        taille (int): _description_
        ordre (str): _description_

    Returns:
        list[int]: _description_
    """

    la_liste = []

    if ordre == "croissant":

        for i in range(0, taille):

            la_liste.append(random.randint(-100, 100))

        la_liste.sort()

    elif ordre == "decroissant":

        for i in range(taille, 0, -1):

            la_liste.append(random.randint(-100, 100))

        la_liste.sort(reverse=True)

    else:

        for i in range(0, taille):

            la_liste.append(random.randint(-100, 100))

    return la_liste

liste_croissante = generer_liste(100, "croissant")
liste_decroissante = generer_liste(100, "decroissant")
liste_quelconque = generer_liste(100, "")

# print(liste_croissante)
# print()
# print(liste_decroissante)
# print()
# print(liste_quelconque)

n = 10_000_000

start_pc = time.perf_counter() # Debut calcul performances

melange_liste(liste_croissante)

end_pc = time.perf_counter() # Fin calcul performances

elapsed_time = end_pc - start_pc

print("Temps écoulé entre les deux mesures :", elapsed_time)
print("Temps estimé pour une instruction :", elapsed_time/n)