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

def perf_mix(fonction1: callable, fonction2: callable, liste_test: list[int], nb_executions: int) -> tuple[float]:

    perfs_fonction1 = []
    perfs_fonction2 = []

    for i in range(0, nb_executions):

        start_perf = time.perf_counter()

        fonction1

        end_perf = time.perf_counter()

        perfs_fonction1.append(end_perf - start_perf)

    moyenne_fonction1 = sum(perfs_fonction1) / nb_executions

    for i in range(0, nb_executions):

        start_perf = time.perf_counter()

        fonction1

        end_perf = time.perf_counter()

        perfs_fonction2.append(end_perf - start_perf)

    moyenne_fonction2 = sum(perfs_fonction2) / nb_executions

    return (moyenne_fonction1, moyenne_fonction2)
