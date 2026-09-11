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

if __name__ == "__main__":
    p1 = Point(3.2, 1)
    print (p1)
    p2 = Point()
    print (p2)
    print(p1.distanceCoordonnee(0,0))

