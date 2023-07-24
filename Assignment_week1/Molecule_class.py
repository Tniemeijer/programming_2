"""
Assignment week 1 Molecule class
Author: T.Niemeijer
Date: 2023-03-25
"""


class Molecule():
    """molecule consisting of atoms"""
    def __init__(self, atom_tup_ls):
        self.composition = atom_tup_ls

    def __repr__(self):
       # would be better to safe this formula once it has been asked for
       # (lazy loading)
       return self.create_formula()
    
    # would be better to also implement __str__, just to be sure
    
    def __add__(self, other):
       return Molecule(self.composition + other.composition)

    def create_formula(self):
       formula ="".join([f'{a[0].symbol}{a[1]}' if a[1] > 1 
                         else f'{a[0].symbol}' 
                         for a in self.composition])
       return formula


