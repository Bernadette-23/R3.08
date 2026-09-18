from personnage import Personnage
from guerrier import Guerrier
from mage import Mage
from joueur import Joueur

if __name__ == '__main__':

    guerrier1 = Guerrier('Gerrier1', 2)
    mage1 = Mage('Mage1', 3)
    print(vars(guerrier1))
    guerrier1.combat(mage1)
    print(f"{guerrier1.get_pseudo()} a {guerrier1.get_pv()} PV et {mage1.get_pseudo()} a {mage1.get_pv()} PV")
    print(guerrier1)
