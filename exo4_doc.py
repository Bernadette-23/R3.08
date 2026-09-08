def affiche(srt1 : str):
    return f"texte à afficher : {srt1}"

class Velo:
    def __init__(self, marque, taille, couleur, vitessemax):
        self.marque = marque
        self.taille = taille
        self.couleur = couleur
        self.vitessemax = vitessemax
        self.vitesse = 1

    def __str__(self):
        return f"Le vélo de la marque {self.marque}, de taille {self.taille} pouce et de couleur {self.couleur}"

    def gear_up(self):
        if 0 < self.vitesse < self.vitessemax:
            self.vitesse = self.vitesse + 1
            print(f"la vitesse vaut actuellement {self.vitesse})

    def gear_down(self):
        if 0 < self.vitesse < self.vitessemax:
            self.vitesse = self.vitesse - 1
            print(f"la vitesse vaut actuellement {self.vitesse})


if __name__ == "__main__":
    str1 = 1, 2, 3, 4, 5
    print(affiche(str1))
    v1 = Velo("Bike","60","vert",6)
    print(v1)
    v1.gear_up()
    print(vars(v1))
    v1.gear_down()
    print(vars(v1))