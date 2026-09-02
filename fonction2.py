n1 = int(input("Entrez le nombre 1 : "))

def seuil (n1 : int, seuil =10):
    if n1 > seuil:
        return f"Le nombre {n1} est supérieur au seuil de {seuil}"
    else:
        return f"le nombre saisi est {n1}"

print(seuil(n1))