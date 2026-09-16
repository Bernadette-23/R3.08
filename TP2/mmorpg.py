class Personnage:

    def __init__(self, pseudo : str, n: int = 1):
        self.__pseudo  = pseudo
        self.__niveau = n
        self.__pv = n
        self.__initiative = n

    def attaquer(self, opposant : Personnage):

        if opposant.__initiative > self.__initiative:
            self.__pseudo -= self.__pv

            if self.__pv > 0:
                self.__opposant -= self.__opposant.pv

        elif opposant.__initiative < self.__initiative:
            self.__opposant -= self.__opposant.__pv

            if self.__oppoqant.__pv > 0:
                self.__pseudo -= self.__pv

        else :
            self.__pseudo -= self.__pv
            self.__opposant -= self.__opposant.__pv

    def combat(self, opposant : Personnage):

        for pv in range opposant.__pv > 0:

            attaquer

        or while self.__pv > 0:





if __name__ == '__main__':
