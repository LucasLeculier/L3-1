# Dictionnaire de poids et tarif par type de lettre
from types import NoneType

COURRIER = {
    "Lettre Verte": {
        20: 1.16,
        100: 2.32,
        250: 4.00,
        500: 6.00,
        1000: 7.50,
        3000: 10.50
    },
    "Lettre Prioritaire": {
        20: 1.43,
        100: 2.86,
        250: 5.26,
        500: 7.89,
        3000: 11.44
    },
    "Ecopli": {
        20: 1.16,
        100: 2.28,
        250: 3.92
    }
}

# Définitions des fonctions

def trouver_affranchissement(type_lettre_choix: str, poids: int) -> float:

    tarif_affranchissement = 0   

    for type_lettre, poids_lettre in COURRIER.items():

        if type_lettre_choix == type_lettre:

            for p, t in poids_lettre.items():
                #print(f"{p}g -> {t} euros\n")

                if poids <= p:
                    tarif_affranchissement = t
                    break
                
                tarif_affranchissement = t
                

    return tarif_affranchissement

def service_poste() -> NoneType:

    while True:
        choix_lettre = input("Choisissez : (Lettre Verte) (Lettre Prioritaire) (Ecopli) : \n")
        if choix_lettre not in COURRIER:
            choix_lettre = input("Ce choix n'existe pas, choisissez (Lettre Verte) (Lettre Prioritaire) (Ecopli) : \n")
        else:
            break
    
    while True:
        try:
            choix_poids = int(input("Entrez le poids de votre lettre en grammes : \n"))
            break
        except:
            print("Poids incorrect.\n")

    le_tarif = trouver_affranchissement(choix_lettre, choix_poids)

    print(f"Votre tarif est de {le_tarif}€. \n")

service_poste()
