"""
Assignment week 1 Chloroplast class
Author: T.Niemeijer
Date: 2023-03-25

refactored by: J. Menzinga
Date: 2023-06-08
"""

from Molecule_class import Molecule
from Atom_class import Atom


class Chloroplast:
    """
    Chloroplast class, a generable symulation of photosynthesis.
    Methods:
        __init__(): initializes the class
        __str__():  returns a string with the current number of water and
                    CO2 molecules
        add_molecule(molecule): adds a molecule to the chloroplast
        photosynthesis(): returns a tuple of 7 glucose molecules and 12
                          oxygen molecules
    """

    def __init__(self):
        self.water = 0
        self.co2 = 0

    def __str__(self):
        info = f'Water: {self.water}\nCO2: {self.co2}'
        return info

    def add_molecule(self, molecule):
        """
        Increases the self.water and self.co2 counters. If the counters
        reach a certain value, the photosynthesis method is called.

        Args:
            molecule (str): a molecule's chemical formula

        Raises:
            ValueError: When the molecule is not H2O or CO2

        Returns:
            res: When photosythesis is triggered, a tuple of 7 glucose
            molecules and 12 oxygen molecules is returned.
            Else, an empty tuple is returned.
        """
        res = ()
        mol_formula = molecule.create_formula()
        match mol_formula:
            case "H2O":
                self.water += 1
            case "CO2":
                self.co2 += 1
            case _: # wildcard, matches anything else
                raise ValueError("I can't work with this..")

        if self.water >= 6 and self.co2 >= 12:
            res = self.photosynthesis()
            self.water -= 6
            self.co2 -= 12
        return res

    def photosynthesis(self):
        """
        Initiates photosynthesis by creating 7 glucose molecules and 12
        oxygen molecules. and then returns a tuple of these molecules.

        Returns:
            tuple: a tuple of 7 glucose molecules and 12 oxygen molecules
        """
        hydrogen = Atom('H', 1, 1)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8)
        glucose = [(carbon, 6), (hydrogen, 12), (oxygen, 6)]
        oxygen = [(oxygen, 2)]
        
        return (Molecule(glucose),) + (Molecule(oxygen),)*6
