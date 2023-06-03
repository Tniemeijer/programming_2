Improvements

In Chloroplast_class.py:
the add_molecule function
First of all has a match with two cases followed by an if statement
it would be better to use case _ for unmatched values instead of a separate if.
Also the function checks wether there are enough resources to perform photosynthesis. This means this add molecules function does more than add molecules. This may become problematic when the simulation becomes more complex, for instance when another factor influences photosynthesis too (for instance if it is nighttime).

