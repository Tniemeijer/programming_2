"""
Main program that creates a Chloroplast that performs photosynthesis under the right circumstances.
Apart from the imports, code is from: https://hanze-hbo-ict.github.io/programming2/week1.2.html
"""

from Chloroplast_class import Chloroplast
from Atom_class import Atom
from Molecule_class import Molecule


hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)


water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
demo = Chloroplast()
els = [water, co2]

while (True):
    print ('\nWhat molecule would you like to add?')
    print ('[1] Water')
    print ('[2] carbondioxyde')
    print ('Please enter your choice: ', end='')
    try:
        choice = int(input())
        res = demo.add_molecule(els[choice-1])
        if (len(res)==0):
            print (demo)
        else:
            print ('\n=== Photosynthesis!')
            print (res)
            print (demo)

    except Exception as e:
        print(f'{e}\n=== That is not a valid choice.')

