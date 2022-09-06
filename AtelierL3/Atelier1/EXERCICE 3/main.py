from math import sqrt

def discriminant(a: float, b: float, c: float):

    return ((b*b) - 4*a*c)

def racine_unique(a: float, b: float):

    return ((-b)/2*a)

def racine_double(a: float, b: float, delta: float, num: float):

    match num:
        case 1:
            return ((-b) + sqrt(delta)/2*a)
        case 2: 
            return ((-b) - sqrt(delta)/2*a)

def str_equation(a: float, b: float, c: float):

    return f"{a}x² + {b}x + {c}=0"


print(racine_double(2, 4, discriminant(2, 4, 1), 1))
print(str_equation(2, 5, 1))