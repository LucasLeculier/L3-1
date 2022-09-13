def ouvrante(car: str) -> bool:
    """Return True si car = "(" ou "[" ou "{"

    Args:
        car (str): _description_

    Returns:
        bool: _description_
    """

    return car in ['(', '[', '{']

def fermante(car: str) -> bool:
    """Return True si car = ")" ou "]" ou "}"

    Args:
        car (str): _description_

    Returns:
        bool: _description_
    """

    return car in [')', ']', '}']

def renverse(car: str) -> str:
    """Renvoie le caractère inverse

    Args:
        car (str): _description_

    Returns:
        str: _description_
    """

    caractère = car

    lst_car = {
        "ouvrant": ['(', '[', '{'],
        "fermant": [')', ']', '}']
    }

    is_ouvrant = ouvrante(car)
    is_fermant = fermante(car)

    if is_ouvrant:

        for i in range(0, len(lst_car.get('ouvrant'))):

            if lst_car.get('ouvrant')[i] == car:

                caractère = lst_car.get('fermant')[i]
    elif is_fermant:

        for i in range(0, len(lst_car.get('fermant'))):

            if lst_car.get('fermant')[i] == car:

                caractère = lst_car.get('ouvrant')[i]

    return caractère

def operateur(car: str) -> bool:
    """Renvoie True si car est un opérateur + ou *

    Args:
        car (str): _description_

    Returns:
        bool: _description_
    """

    return car in ["+", "*", "-"]

def nombre(car: str) -> bool:
    """Renvoie True si car est bien un nombre sinon False

    Args:
        car (str): _description_

    Returns:
        bool: _description_
    """

    return car.isdigit()

def caractere_valide(car: str) -> bool:
    """Renvoie True si le caractère est un caractère valide dans
    une expression arithmetique

    Args:
        car (str): _description_

    Returns:
        bool: _description_
    """

    return ouvrante(car) or fermante(car) or operateur(car) or nombre(car)

def verif_parenthese(expression: str) -> bool:
    """Renvoie True si l'expression arithmetique expression est valide

    Args:
        expression (str): _description_

    Returns:
        bool: _description_
    """

    pile = []

    valide = True

    i = 0

    # print(len(expression))

    while valide and i < len(expression): 

        e = expression[i]

        # print("i :", i)

        # print(e)
        # print(valide)

        if ouvrante(e):

            pile.append(e)

        elif fermante(e):

            if not pile:

                valide =  False
            
            else:
                
                h = pile.pop()

                if e != renverse(h):

                    valide = False

        # print("La pile :", pile)

        i += 1

    if pile:

        valide = False


    return valide



if __name__ == "__main__":

    print(ouvrante("(")) # Doit renvoyer True
    print(ouvrante(")")) # Doit renvoyer False

    print()

    print(fermante("(")) # Doit renvoyer False
    print(fermante(")")) # Doit renvoyer True

    print()

    print(renverse(")"))
    print(renverse("["))
    print(renverse("+"))

    print()

    print(operateur("+"))
    print(operateur(")"))

    print()

    print(nombre("456"))
    print(nombre("("))

    print()

    print(caractere_valide("a")) # False
    print(caractere_valide("+")) # True
    print(caractere_valide("{")) # True

    print()

    print(verif_parenthese("(3+2)*6-1")) # True
    print(verif_parenthese("((3+2)*6-1")) # False
    print(verif_parenthese("(5+7]*12")) # False
    print(verif_parenthese("((5+4)*(6+7))")) # False