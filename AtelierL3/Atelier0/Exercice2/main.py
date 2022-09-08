from math import ceil

# Dictionnaire de poids (en grammes) et tarif par type de lettre
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

ZONES_COMPLEMENTS = {
    "Lettre Verte": {
        "FM": 0,
        "OM1": 0.05,
        "OM2": 0.11
    },
    "Lettre Prioritaire": {
        "FM": 0,
        "OM1": 0.05,
        "OM2": 0.11
    },
    "Ecopli": {
        "FM": 0,
        "OM1": 0.02,
        "OM2": 0.05
    }
}

# Définitions des fonctions

def trouver_affranchissement(type_lettre_choix: str, poids: int) -> float:
    """Fonction permettant de trouver le taux d'affranchissement du client selon le poids du courrier et de son type passés en paramètres 
    effectifs

        params:
            type_lettre_choix: Le type de lettre souhaité
            poids: Le poids de la lettre
        
        returns:
            tarif_affranchissement: Renvoie le tarif d'affranchissement correspondant 
                                    à la lettre de type_lettre_choix et selon son poids
    """

    tarif_affranchissement = 0   

    # On parcours le dictionnaire pour avoir le type de lettre et leurs tarifs
    for type_lettre, poids_lettre in COURRIER.items():

        if type_lettre_choix == type_lettre:

            # p poids, t tarif
            for p, t in poids_lettre.items():
                #print(f"{p}g -> {t} euros\n")

                if poids <= p:
                    tarif_affranchissement = t
                    break
                
                tarif_affranchissement = t
                

    return tarif_affranchissement

def service_poste() -> None:
    """Procédure demandant à l'utilisateur de rentrer le type de lettre et son poids, affiche le tarif d'affranchissement correspondant
        uniquement si le type de lettre existe et si le poids est valide

        returns:
            None
    
    """

    choix_lettre = input("Choisissez : (Lettre Verte) (Lettre Prioritaire) (Ecopli) : \n")
    
    while True:
        
        if choix_lettre not in COURRIER:
            choix_lettre = input("Ce choix n'existe pas, choisissez (Lettre Verte) (Lettre Prioritaire) (Ecopli) : \n")
        else:
            break

    poids_message = "Entrez le poids de votre lettre en grammes : \n"

    # Boucle pour demander à l'utilisateur de renseigner le poids de la lettre, poids devant etre valide
    while True:
        
        choix_poids = input(poids_message) 
        
        try:
            choix_poids = int(choix_poids) # Le choix du poids doit etre un entier, on tente donc de convertir la chaine de caractere
                                            # de l'input en entier et on change le message dans le cas d'une exception
            
            if choix_poids <= 0: # Le poids doit etre positif supérieur à 0
                poids_message = "Ce poids est invalide, veuillez entrer un poids valide entier et supérieur à 0 : \n"
            else:
                break

        except:
            poids_message = "Ce poids est invalide, veuillez entrer un poids valide entier et supérieur à 0 : \n"
    
    # Boucle pour envoi outre mer ou non
    choix_zone = input("Choisissez la zone dans laquelle envoyer votre courrier entre (FM) (OM1) (OM2) : \n")
    
    while True:

        if choix_zone in ZONES_COMPLEMENTS[choix_lettre].keys():
            break

        else:
            choix_zone = input("Cette zone n'existe pas, entrez une zone valide entre (FM) (OM1) (OM2) : \n")

    for zones, complement in ZONES_COMPLEMENTS[choix_lettre].items():
                    
        if choix_zone == zones:
                        
            tranche = ceil(choix_poids / 10)
            le_tarif = trouver_affranchissement(choix_lettre, choix_poids) + tranche * complement

    print(f"Votre tarif est de {le_tarif}€. \n")

# Appel de la fonction du service de poste pour lancer l'execution du programme
service_poste()
