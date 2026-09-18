class Personnage:

    def __init__(self, pseudo : str, n: int = 1):
        self.__pseudo  = pseudo
        self.__niveau = n
        self.__pv = n
        self.__initiative = n


    def attaquer(self, opposant : Personnage):

        if self.__initiative > opposant.__initiative:
            opposant.__pv -= self.__niveau
            if opposant.__pv > 0:
                self.__pv -= opposant.__niveau

        elif opposant.__initiative > self.__initiative:
            self.__pv -= opposant.__niveau
            if self.__pv > 0:
                opposant.__pv -= self.__niveau

        else:
            self.__pv -= opposant.__niveau
            opposant.__pv -= self.__niveau

    def combat(self, opposant : Personnage):

         while self.__pv > 0 and opposant.__pv > 0:
             self.attaquer(opposant)

    def soigner(self):
         self.__pv =  self.__niveau

class Guerrier(Personnage):

    def __init__(self, pseudo : str, n: int = 1):
        super().__init__(pseudo, n)
        self.set_pv(n * 8 +4)
        self.set_initiative(n *4 +6)



class Mage(Personnage):

    def __init__(self, pseudo: str, n: int = 1):
        super().__init__(pseudo, n)
        self.set_pv(n *5 +10)
        self.set_initiative(n * 6+4)
        self.__mana = n*5





if __name__ == '__main__':
    gerrier1 = Guerrier('Gerrier1', 2)
    mage1 = Mage('Mage1', 3)
    gerrier1.attaquer(mage1)
    mage1.combat(gerrier1)