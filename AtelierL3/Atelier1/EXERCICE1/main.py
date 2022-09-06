"""
def message_imc(imc: float):
    
    if imc < 16.5:
        return "dénutrition ou famine \n"
    elif imc >= 16.5 and imc < 18.5:
        return "maigreur"
    elif imc >= 18.5 and imc < 25:
        return "corpulence normale \n"
    elif imc >= 25 and imc < 30:
        return "surpoids \n"
    elif imc >= 30 and imc < 35:
        return "obésité \n"
    elif imc >= 35 and imc < 40:
        return "obésité sévère \n"
    elif imc > 40:
        return "obésité morbide \n"
"""

imc_val = [16.5, 18.5, 25, 30, 35, 40]
imc_message = ["dénutrition ou famine", "maigreur", "corpulence normale", "surpoids", "obésité", "obésité sévère", "obésité morbide"]

def message_imc(imc: float, imc_val: list, imc_message: list):

    counter = 0

    #for i in range()

def test_imc():

    print(message_imc(15.0)) # denutrition ou famine
    print(message_imc(34.0)) # obésité
    print(message_imc(50.0)) # obésité morbide
    print(message_imc(18.5)) # corpulence normale
    print(message_imc(31.0)) # obésité

test_imc()
    

