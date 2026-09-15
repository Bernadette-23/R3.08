class Tasse:

    matiere : str = "céramique"

    def __init__(self, couleur, contenance, marque):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        return f"La tasse de matiere {Tasse.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml"

    def contenu(self,contenu):
        self.contenu = contenu

    def bue(self):
        del(self.contenu)

if __name__ == "__main__":
    mc = Tasse("bleu","50","duralex")
    print(mc)
    print(vars(mc))
    mc.contenu("eau")
    print(mc.contenu)
    print(vars(mc))
    mc.bue()
    print(vars(mc))
