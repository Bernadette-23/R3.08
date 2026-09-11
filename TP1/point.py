class Point:
  #  x : float=0
   # y : float=0
    def __init__(self, x : int=0, y : int=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Piont : [{self.__x} ; {self.__y}]"

if __name__ == "__main__":
    p1 = Point(3.2, 1)
    print (p1)
    p2 = Point()
    print (p2)

