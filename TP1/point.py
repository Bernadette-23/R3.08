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

 #   def distancePoint(self, camarade : Point):

class Cercle:

    def __init__(self,centre:Point, rayon:int):
        self.__centre = Point(centre)
        self.__rayon = rayon

    def diametre(self,diametre:int):
        self.__diametre = 2*self.__rayon
        return diametre

    def perimetre(self,perimetre:int):
        self.__perimetre = 2*self.__rayon*3.14
        return perimetre

    def surface(self,surface:int):
        self.__surface = 3.14*(self.__rayon*self.__rayon)
        return surface

    def intersection(self,):
        ddfzfz

    def partie(self):
        gdfkd



if __name__ == "__main__":
    p1 = Point(3.2, 1)
    print (p1)
    p2 = Point()
    print (p2)
    print(p1.distanceCoordonnee(0,0))

