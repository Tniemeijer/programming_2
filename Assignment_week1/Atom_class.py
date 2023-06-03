"""
Assignment week 1 Class Atom
Author: T.Niemeijer
Date: 2023-03-25
"""

class Atom:
    """Representation of an element of the periodic table"""
    def __init__(self, symbol, molecular_nr, neutrons):
        self.symbol = symbol
        self.mol_number = molecular_nr 
        self.neutrons = neutrons
    
    def __eq__(self, other):
        self.check_mol_number(other)
        return self.mass_number() == other.mass_number()

    def __lt__(self, other):
        self.check_mol_number(other)
        return self.mass_number() < other.mass_number()

    def __gt__(self, other):
        self.check_mol_number(other)
        return self.mass_number() > other.mass_number()
    
    def __le__(self, other):
        self.check_mol_number(other)
        return self.mass_number() <= other.mass_number()

    def __ge__(self, other):
        self.check_mol_number(other)
        return self.mass_number() >= other.mass_number()

    def proton_number(self):
        return self.mol_number

    def mass_number(self):
        return self.mol_number + self.neutrons

    def isotope(self, new_neutron_nr):
        self.neutrons = new_neutron_nr

    def check_mol_number(self, other):
        if self.mol_number != other.mol_number:
            raise Exception


