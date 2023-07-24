"""
Assignment week 1 Chloroplast class
Author: T.Niemeijer
Date: 2023-03-25
"""

from Molecule_class import Molecule
from Atom_class import Atom

class Chloroplast:
    """Chloroplast, does photosynthesis and stuff"""
    def __init__(self):
        self.water = 0
        self.co2 = 0

    def __str__(self):
        # could be made into a one-liner
        info = f'Water: {self.water}\nCO2: {self.co2}'
        return info

    def add_molecule(self, molecule):
        res = ()
        mol_formula = molecule.create_formula() #<-- could just call molecule.__str__()
        # also better to uppercase the result, just to be sure
        match mol_formula:
            case "H2O":
                self.water += 1
            case "CO2": 
                self.co2 += 1
            case _:
                res = ()
                raise ValueError("I can't work with this..")
        if self.water >= 6 and self.co2 >= 12:
            res = self.photosynthesis()
            self.water -= 6
            self.co2 -= 12
        # This is incorrect
        # you should return a list of tuples, not a tuple
        return res
    
    def photosynthesis(self):
        hydrogen = Atom('H', 1, 1)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8) 
        glucose = [(carbon, 6),(hydrogen, 12), (oxygen, 6)]
        oxygen = [(oxygen, 2)]
        return (Molecule(glucose),) + (Molecule(oxygen),)*6 





       
