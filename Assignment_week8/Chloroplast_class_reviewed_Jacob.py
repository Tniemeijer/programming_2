"""
Assignment week 1 Chloroplast class
Author: T.Niemeijer
Date: 2023-03-25
"""

from Molecule_class import Molecule
from Atom_class import Atom

class Chloroplast:
    """Chloroplast, does photosynthesis and stuff"""     # The docstrings could be a bit more detailed.
    def __init__(self):
        self.water = 0
        self.co2 = 0

    def __str__(self):
        info = f'Water: {self.water}\nCO2: {self.co2}'
        return info

    def add_molecule(self, molecule):
        res = ()
        # Not sure if it's neccecary here but it might be usefull to first convert mol_formula to upper/lower case to prevent errors        
        mol_formula = molecule.create_formula()
        match mol_formula: # Very nice use of new features!
            case "H2O":
                self.water += 1
            case "CO2": 
                self.co2 += 1
        if mol_formula != 'H2O' and mol_formula != 'CO2': # Considering you already match for the two inputs that work, this could just be an elsestatement instead of an if and statement
            res = () # I think this is nunecessary, considering you already initialised res as an empty tuple
            raise ValueError("I can't work with this..")
        if self.water >= 6 and self.co2 >= 12:
            res = self.photosynthesis()
            self.water -= 6
            self.co2 -= 12
        return res
    
    def photosynthesis(self):
        hydrogen = Atom('H', 1, 1)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8) 
        glucose = [(carbon, 6),(hydrogen, 12), (oxygen, 6)]
        oxygen = [(oxygen, 2)]
        return (Molecule(glucose),) + (Molecule(oxygen),)*6 





       
