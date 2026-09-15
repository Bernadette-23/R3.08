def division(dividande : float, diviseur : float) -> float:
    if diviseur == 0 :
        raise ZeroDivisionError ("le diviseur est nul")
    else:
        return diviseur / dividande

if __name__ == "__main__":
    try:
        res = division(5,10)
    except:
        print("erreur détectée")
    else:
        print(res)
