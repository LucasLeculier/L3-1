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

    

if __name__ == "__main__":

    print(ouvrante("(")) # Doit renvoyer True
    print(ouvrante(")")) # Doit renvoyer False

    print()

    print(fermante("(")) # Doit renvoyer False
    print(fermante(")")) # Doit renvoyer True

    print()