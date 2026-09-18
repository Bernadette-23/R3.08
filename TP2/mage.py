from personnage import Personnage

class Mage(Personnage):

    def __init__(self, pseudo: str, n: int = 1):
        super().__init__(pseudo, n)
        self.set_pv(n *5 +10)
        self.set_initiative(n * 6+4)
        self.__mana = n*5

    def get_mana(self):
        return self.__mana

    def set_mana(self, valeur):
        self.__mana = valeur

    def degats(self):
        if self.get_mana() >= 4:
            self.set_mana = self.get_mana() - 4
            return self.get_niveau() + 3
        return self.get_niveau()