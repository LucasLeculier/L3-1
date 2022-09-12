import os

def full_name(str_arg: str) -> str:
    """Renvoie une chaine de caractères avec le NOM
    en majuscules et le prenom en minuscule avec la premiere lettre
    en majuscules

    Args:
        str_arg (str): _description_

    Returns:
        str: _description_
    """

    new_str = ""
    le_nom_prenom = str_arg.split(" ")

    new_str += le_nom_prenom[0].upper() + " " + le_nom_prenom[1][0].upper() + le_nom_prenom[1][1:]

    return new_str

# str_variable2test = 'bisgambiglia paul'
# print(full_name(str_variable2test))

def is_mail(str_arg: str) -> tuple[int]:
    """Vérifie si l'adresse email est valide et renvoie un tuple correspondant
    à la validité ou non de l'adresse

    Args:
        str_arg (str): _description_

    Returns:
        tuple[int]: _description_
    """

    validity_list = [0, 0]

    if "@" in str_arg:

        adresse = str_arg.split("@")
        corps_adresse = adresse[0]
        domaine_adresse = adresse[1]

        
        if "." in domaine_adresse:

            if corps_adresse and "." != corps_adresse[0] and "." != corps_adresse[-1]:

                if "." != domaine_adresse[0] and "." != domaine_adresse[-1]:

                    validity_list = [1, 0]
                
                else:
                    validity_list = [0, 3]

            else:
                validity_list = [0, 1]

        else:
            validity_list = [0, 4]

    else:
        validity_list = [0, 2]

    validity_tuple = (validity_list[0], validity_list[1])

    return validity_tuple

"""
str_variable2test = 'bisgambiglia_paul@univ-corse.fr'
print(is_mail(str_variable2test)) # doit renvoyer (1,0)
str_variable2test = 'bisgambiglia_paulOuniv-corse.fr'
print(is_mail(str_variable2test)) # doit renvoyer (0,2)
str_variable2test = 'bisgambiglia_paul@univ-corsePOINTfr'
print(is_mail(str_variable2test)) # doit renvoyer (0,4)
str_variable2test = '@univ-corse.fr'
print(is_mail(str_variable2test)) # doit renvoyer (0,1)
"""

def mots_n_lettres(lst_mots: list[str], n: int) -> list[str]:
    """Renvoie une liste de mots de lst_mots contenant exactement n lettres

    Args:
        lst_mots (list[str]): _description_
        n (int): _description_

    Returns:
        list[str]: _description_
    """

    return [mot for mot in lst_mots if len(mot) == n]

def commence_par(mot: str, prefixe: str) -> bool:
    """Renvoie True si mot commence par prefixe sinon False

    Args:
        mot (str): _description_
        prefixe (str): _description_

    Returns:
        bool: _description_
    """

    starts_with = False

    if len(mot) >= len(prefixe):

        if prefixe == mot[0:len(prefixe)]:
            starts_with = True
    
    return starts_with

def finit_par(mot: str, suffixe: str) -> bool:
    """Renvoie True si mot se termine par suffixe sinon False

    Args:
        mot (str): _description_
        suffixe (str): _description_

    Returns:
        bool: _description_
    """

    ends_with = False

    if len(mot) >= len(suffixe):

        if suffixe == mot[-len(suffixe):]:
            ends_with = True
    
    return ends_with

def finissent_par(lst_mot: list[str], suffixe: str) -> list[str]:
    """Renvoie la liste de tous les mots contenus dans lst_mot qui se terminent
    par suffixe

    Args:
        lst_mot (list[str]): _description_
        suffixe (str): _description_

    Returns:
        list[str]: _description_
    """

    return [mot for mot in lst_mot if finit_par(mot, suffixe)]

def commencent_par(lst_mot: list[str], prefixe: str) -> list[str]:
    """Renvoie la liste de tous les mots contenus dans lst_mot qui commencent pas prefixe

    Args:
        lst_mot (list[str]): _description_
        prefixe (str): _description_

    Returns:
        list[str]: _description_
    """

    return [mot for mot in lst_mot if commence_par(mot, prefixe)]

def liste_mots(lst_mot: list[str], prefixe: str, suffixe: str, n) -> list[str]:
    """Renvoie la liste des mots de lst_mot qui commencent par prefixe, se terminent par suffixe
    et qui contiennent exactement n lettres

    Args:
        lst_mot (list[str]): _description_
        prefixe (str): _description_
        suffixe (str): _description_
        n (_type_): _description_

    Returns:
        list[str]: _description_
    """

    return 

def dictionnaire(fichier: str) -> list[str]:
    """Renvoie la liste des mots présents dans fichier

    Args:
        fichier (str): _description_

    Returns:
        list[str]: _description_
    """

    f = open(fichier, "r")
    ligne = f.readline().rstrip()

    liste_de_mots = []

    while ligne:
        liste_de_mots.append(ligne)
        ligne = f.readline().rstrip()

    return liste_de_mots

    

lst_mot = ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
"finir", "aimer"]

def test_exercice1():
    print()

    print(mots_n_lettres(lst_mot, 7))
    print("Résultat attendu :", ['bonjour', 'pouvoir', 'abajour'], "\n")

    print(commence_par("pouvoir", "pouv"))
    print("Résultat attendu :", "True", "\n")

    print(finit_par("pouvoir", "voir"))
    print("Résultat attendu :", "True", "\n")

    print(finissent_par(lst_mot, "our"))
    print("Résultat attendu :", ["bonjour", "jour", "cour", "abajour"], "\n")
        
    print(commencent_par(lst_mot, "jou"))
    print("Résultat attendu :", ["jouer", "jour"], "\n")

    print(liste_mots(lst_mot, "bon", "our", 7))
    print("Résultat attendu :", ["bonjour"], "\n")

    print(dictionnaire("AtelierL3\Atelier3\mots.txt"))
    print("Résultat attendu :", ["Python", "Java", "Javascript", "PHP", "Csharp", "Cplusplus", "C"], "\n")

test_exercice1()