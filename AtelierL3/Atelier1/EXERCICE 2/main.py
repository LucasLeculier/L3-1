def est_bissextile(annee: int):

    return annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0

def test():
    
    print(f"2015 ? {est_bissextile(2015)} \n")
    print(f"2016 ? {est_bissextile(2016)} \n")
    print(f"1945 ? {est_bissextile(1945)} \n")
    print(f"2032 ? {est_bissextile(2032)} \n")
    print(f"2400 ? {est_bissextile(2400)} \n")
    print(f"2000 ? {est_bissextile(2000)} \n")

test()