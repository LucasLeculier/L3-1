from math import ceil

"""
Fonction calcule prix
Fonction pour recuperer les prix
Fonction principale pour executer le programme
"""

# Dictionnaire contenant les données des types de courrier et des tarifs
COURRIER = {
    "Lettre Verte": {
        "tarifs": {
            20: 1.16,
            100: 2.32,
            250: 4.00,
            500: 6.00,
            1000: 7.50,
            3000: 10.50
        },
        "complement": {
            "FM": 0,
            "OM1": 0.05,
            "OM2": 0.11
        }
    },
    "Lettre Prioritaire": {
        "tarifs": {
            20: 1.43,
            100: 2.86,
            250: 5.26,
            500: 7.89,
            3000: 11.44
        },
        "complement": {
            "FM": 0,
            "OM1": 0.05,
            "OM2": 0.11
        },
    },
    "Ecopli": {
        "tarifs": {
            20: 1.16,
            100: 2.28,
            250: 3.92
        },
        "complement": {
            "FM": 0,
            "OM1": 0.02,
            "OM2": 0.05
        }
    }
}

"""
ZONES_DETAIL = {
    "FM": ["France", "Monaco", "Andorre"],
    "OM1": ["Guyane", "Guadeloupe", "Martinique", "LaRéunion", "StPierreetMiquelon", "St Barthélémy", "St-Martin", "Mayotte"],
    "OM2": ["Nouvelle-Calédonie", "Polynésiefrançaise", "Wallis-et-Futuna", "T.A.A.F"]
}
"""

ZONES = ["FM", "OM1", "OM2"]

def choix_client() -> tuple:
    """Demande à l'utilisateur de rentrer un type de lettre, une zone ou envoyer la
    lettre et le poids de cette lettre et renvoie un tuple contenant les valeurs
    saisies
    
    :return: (choix_lettre, choix_zone, choix_poids)(tuple)
    """

    choix_lettre = input("Choisissez le type de lettre : \n 1. Lettre Verte\n 2. Lettre Prioritaire\n 3. Ecopli\n")

    while True:

        if choix_lettre not in COURRIER:
            choix_lettre = input("Ce choix n'existe pas, choisissez le type de lettre : \n 1. Lettre Verte\n 2. Lettre Prioritaire\n 3. Ecopli\n ")
        else:
            break

    choix_zone = input("Choisissez une zone ou envoyer votre courrier : \n 1. FM \n 2. OM1 \n 3. OM2 \n")

    while True:

        if choix_zone not in ZONES:
            choix_zone = input("Ce choix n'existe pas, choisissez une zone ou envoyer votre courrier : \n 1. FM \n 2. OM1 \n 3. OM2 \n")
        else:
            break

    poids_message = "Entrez le poids de votre lettre en grammes : \n"

    # Boucle pour demander à l'utilisateur de renseigner le poids de la lettre, poids devant etre valide
    while True:
        
        choix_poids = input(poids_message) 
        
        try:
            choix_poids = float(choix_poids) # Le choix du poids doit etre un entier, on tente donc de convertir la chaine de caractere
                                            # de l'input en entier et on change le message dans le cas d'une exception
            
            if choix_poids <= 0: # Le poids doit etre positif supérieur à 0
                poids_message = "Ce poids est invalide, veuillez entrer un poids valide supérieur à 0 : \n"
            else:
                break

        except:
            poids_message = "Ce poids est invalide, veuillez entrer un poids valide supérieur à 0 : \n"

    return (choix_lettre, choix_zone, choix_poids)

def prix_net(type_lettre: str, poids: float) -> float:
    """Calcule le prix net en fonction du type de la lettre et de son poids
    
    :param type_lettre(str): sss
    :param poids(float): sss
    :return: (float)
    """

    #prix = 0.0

    for key, value in COURRIER.items():

        if type_lettre == key:
            print(value)
  
            for p, t in value.get("tarifs").items():

                if poids <= p:
                    tarif_affranchissement = t
                    break
                    
                tarif_affranchissement = t

    return tarif_affranchissement

def prix_complement(type_lettre: str, zone_lettre: str, poids: float, prix_net: float) -> float:

    prix = 0.0

    complement = 0.0

    for key, value in COURRIER.items():

        if type_lettre == key:

            for c, t in value.get("complement").items():

                if zone_lettre == c:

                    complement = t

    tranche = ceil(poids / 10)

    prix = prix_net + tranche * complement

    return prix

def main():

    choix = choix_client()

    print("Le prix a payer est de :", prix_complement(choix[0], choix[1], choix[2], prix_net=prix_net(choix[0], choix[2])))


main()