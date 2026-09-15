import math

class Point:

    def __init__(self, x : int=0, y : int=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Piont : [{self.__x} ; {self.__y}]"

    def distanceCoordonnee(self, x:float,y:float):
        distance = (math.sqrt((self.__x-x)**2 + (self.__y-y)**2)) # cette ligne peut etre remplacer par les 2 prochaines lignes

                  # 1ère option --> (math.pow(self.__x-x,2) + math.pow(self.__y-y,2))
                  # 2eme option --> ((self.__x-x)*(self.__x-x) + (self.__y-y)*(self.__y-y))
        return distance

    def distancePoint(self, camarade : Point) -> float:
        return ((self.__x - camarade.__x) ** 2 + (self.__y - camarade.__y) ** 2) ** 0.5

class Cercle:

    def __init__(self,rayon:int, centre:Point ):
        self.__rayon = rayon
        self.__centre = Point(centre)

    def diametre(self):
        return 2*self.__rayon


    def perimetre(self):
        return 2*self.__rayon*3.14

    def surface(self):
        return 3.14*(self.__rayon*self.__rayon)


    def intersection(self,autre:Cercle):
        if self.__centre.distancePoint(autre.__centre) < (self.__rayon + autre.__rayon):
            return True
        else:
            return False

    def partie(self, A: Point) -> bool:
        return self.__centre.distancePoint(A) <= self.__rayon


class Rectangle:

    def __init__(self, basGauche=None, longueur=None, hauteur=None, hautDroit=None):

        if basGauche is None and hautDroit is None:
            self.__basGauche = Point(0, 0)
            self.__longueur = 1
            self.__hauteur = 1

        elif hautDroit is None:
            self.__basGauche = basGauche
            self.__longueur = longueur
            self.__hauteur = hauteur

        else:
            self.__basGauche = basGauche
            self.__longueur = hautDroit.x - basGauche.x
            self.__hauteur = hautDroit.y - basGauche.y

    def surfaceR(self):
        return  self.__longueur*self.__hauteur

    def perimetreR(self):
        return 2*(self.__longueur+self.__hauteur)

    def getBasGauche(self):
        return self.__basGauche

    def getBasDroite(self):
        return Point(self.__basGauche.x + self.__longueur, self.__basGauche.y)

    def getHautGauche(self):
        return Point(self.__basGauche.x, self.__basGauche.y + self.__hauteur)

    def getHautDroite(self):
        return Point(self.__basGauche.x + self.__longueur,
                     self.__basGauche.y + self.__hauteur)

    def contient(self, A: Point):
        return (self.__basGauche.x <= A.x <= self.__basGauche.x + self.__longueur and
                self.__basGauche.y <= A.y <= self.__basGauche.y + self.__hauteur)


class TriangleRectangle:

    def __init__(self, origine: Point = Point(0,0), longueur: float = 1, hauteur: float = 1):
        self.__origine = origine
        self.__longueur = longueur
        self.__hauteur = hauteur

    def surface(self):
        return (self.__longueur * self.__hauteur) / 2

    def perimetre(self):
        hypotenuse = ((self.__longueur)**2 + (self.__hauteur)**2)**0.5
        return self.__longueur + self.__hauteur + hypotenuse

    def getOrigine(self):
        return self.__origine

    def getPointLongueur(self):
        return Point(self.__origine.x + self.__longueur, self.__origine.y)

    def getPointHauteur(self):
        return Point(self.__origine.x, self.__origine.y + self.__hauteur)

    def contient(self, A: Point):
        if not (self.__origine.x <= A.x <= self.__origine.x + self.__longueur and
                self.__origine.y <= A.y <= self.__origine.y + self.__hauteur):
            return False
        pente = -self.__hauteur / self.__longueur
        y_max = pente * (A.x - self.__origine.x) + (self.__origine.y + self.__hauteur)
        return A.y <= y_max

if __name__ == "__main__":
    p1 = Point(3.2, 1)
    print (p1)
    p2 = Point()
    print (p2)
    print(p1.distanceCoordonnee(0,0))

