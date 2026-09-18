class Personnage:

    def __init__(self, pseudo : str, n: int = 1):
        self.__pseudo  = pseudo
        self.__niveau = n
        self.__pv = n
        self.__initiative = n

    def __str__(self):
        return f"Personnage {super().__str__()}"


    def get_niveau(self):
        return self.__niveau

    def get_pseudo(self):
        return self.__pseudo

    def get_pv(self):
        return self.__pv

    def get_initiative(self):
        return self.__initiative

    def set_pv(self, pv):
        self.__pv = pv

    def set_initiative(self, initiative):
        self.__initiative = initiative


    def degats(self):
        return self.__niveau

    def attaquer(self, opposant : Personnage):

        if self.__initiative > opposant.__initiative:
            opposant.__pv -= self.degats()
            if opposant.__pv > 0:
                self.__pv -= opposant.degats()

        elif opposant.__initiative > self.__initiative:
            self.__pv -= opposant.degats()
            if self.__pv > 0:
                opposant.__pv -= self.degats()

        else:
            self.__pv -= opposant.degats()
            opposant.__pv -= self.degats()

    def combat(self, opposant : Personnage):

         while self.__pv > 0 and opposant.__pv > 0:
             self.attaquer(opposant)

    def soigner(self):
         self.__pv =  self.__niveau

