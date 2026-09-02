n1 = int(input("Entrez le nombre 1 : "))
n2 = int(input("Entrez le nombre 2 : "))

def max (n1 : int, n2 :int) -> int :
    if n1 > n2:
        return n1
    else:
        return n2

print(max(n1, n2))

"""
--> fil d'execution 
if __name__=="__main__":
    val1 = int(input("saisir un entier"))
    val2 = int(input("saisir un entier"))
    
    print(max (val1,val2))
"""