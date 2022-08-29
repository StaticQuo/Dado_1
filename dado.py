import random as rd

def dado():
    cara = rd.randrange(1, 6)
    if cara == 1:
        return "uno"
    if cara == 2:
        return "dos"
    if cara == 3:
        return "tres"
    if cara == 4:
        return "cuatro"
    if cara == 5:
        return "cinco"
    if cara == 6:
        return "seis"

dado()

tirada = dado()

print(f"el resultado de la tirada es: {tirada}")