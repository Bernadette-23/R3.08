from personnage import Personnage

class Guerrier(Personnage):

    def __init__(self, pseudo : str, n: int = 1):
        super().__init__(pseudo, n)
        self.set_pv(n * 8 +4)
        self.set_initiative(n *4 +6)

    def __str__(self):
        return f"Guerrier {super().__str__()}"

    def degats(self):
        return self.get_niveau() * 2