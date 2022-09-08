from datetime import date

ANNEE_MIN = 1900
ANNEE_MAX = 2022

# Renvoie True si l'année est bissextile, False au contraire
def est_bissextile(a: int) -> bool:
    """Cette fonction prend en paramètre un entier correspondant à une année (ex. 2000) et renvoie True si elle est
    bissextile sinon false
    
    """

    return a % 4 == 0 and a % 100 != 0 or a % 400 == 0

# Renvoie True si la date est valide 
def date_est_valide(j: int, m: int, a: int) -> bool:

    jours_en_fevrier = 28

    if est_bissextile(a):
        jours_en_fevrier = 29

    # Contient des listes représentant chaque en tant que des couples [a, b] ou a est le numéro du mois et b le nombre maximum de jours de ce mois dans l'année
    max_jours_mois = [ [1, 31], [2, jours_en_fevrier], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31] ]

    if ANNEE_MIN <= a <= ANNEE_MAX:   
        # On parcours le tableau des mois et de leur maximum de jours
        for e in max_jours_mois:

            # On cherche le mois qui correspond au mois rentré
            if m == e[0]:

                # On return True si le jour existe de 1 au maximum de jours du mois sinon False
                return 0 < j <= e[1]

    # Si le nombre rentré pour mois = m n'est compté parmis les 12 mois existants alors la date est erronée
    return False

# Permet la saisie de la date de naissance de l'utilisateur
def saisie_date_naissance() -> date:

    while True:

        # On fait cela simplement pour rendre cet exercice un peu plus interactif pour l'utilisateur
        saisie = input("Entrez votre date de naissance au format j/m/aaaa : \n")

        # On coupe la chaine de caractères en trois chaines differentes qui correspondent à jours, mois et année
        jour = int(saisie.split("/")[0])
        mois = int(saisie.split("/")[1])
        annee = int(saisie.split("/")[2])

        if date_est_valide(jour, mois, annee):
            # Renvoi une liste contenant le jour, le mois et l'année de naissance entrée
            return date(annee, mois, jour)
        else:
            print("Cette date de naissance est invalide.")

# Renvoi l'age actuel de la personne née a la date passée en argument
def age(date_naissance: date) -> int:

    # Date d'aujourd'hui
    ajd = date.today()

    # Renvoi la différence, l'age de la personne en années
    return int((ajd - date_naissance).days / 365)

# Renvoi True si l'individu est majeur (>= 18) sinon False
def est_majeur(date_naissance: date) -> int:

    return age(date_naissance) >= 18

# Procédure de tests, print si vous etes autorisé à entrer si vous etes majeur
def test_acces() -> None:

    date_naissance = saisie_date_naissance()

    if est_majeur(date_naissance):
        print(f"Bonjour, vous avez {age(date_naissance)} ans, Accès autorisé !\n")
    else:
        print(f"Désolé, vous avez {age(date_naissance)} ans, Accès refusé !\n")


#print(date_est_valide(29, 2, 1945))

#print(est_majeur(saisie_date_naissance()))

test_acces() 
""" exemples tests
1/9/2000 -> autorisé
1/9/2004 -> autorisé
1/9/2005 -> refusé
"""