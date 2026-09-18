class Joueur:

    def __init__(self, nom : str, nmax : int):
        self.__nom = nom
        self.__nmax = nmax
        self.__personnages = []

    def get_nom(self):
        return self.__nom

    def get_nmax(self):
        return self.__nmax

    def get_personnages(self):
        return self.__personnages

    def ajouter_personnage(self, personnage):
        if len(self.__personnages) < self.__nmax:
            self.__personnages.append(personnage)

