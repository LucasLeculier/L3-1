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

                if "." != corps_adresse[0] and "." != corps_adresse[-1]:

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

str_variable2test = 'bisgambiglia_paul@univ-corse.fr'
print(is_mail(str_variable2test)) # doit renvoyer (1,0)
str_variable2test = 'bisgambiglia_paulOuniv-corse.fr'
print(is_mail(str_variable2test)) # doit renvoyer (0,2)
str_variable2test = 'bisgambiglia_paul@univ-corsePOINTfr'
print(is_mail(str_variable2test)) # doit renvoyer (0,4)
str_variable2test = '@univ-corse.fr'
print(is_mail(str_variable2test)) # doit renvoyer (0,1)