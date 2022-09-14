from typing import Callable


def present(lst: list, e: int) -> bool:
    """Renvoie True si lst contient e sinon False

    Args:
        lst (list): _description_
        e (int): _description_

    Returns:
        bool: _description_
    """

    return e in lst

def test_present(present: Callable) -> None:

    print()

if __name__ == '__main__':


    test_present(present([1, 2, 4, 6, 1, 3], 1))