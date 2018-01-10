from utils import *
import re

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    
    for i, field in enumerate(values):
        #distinctValuesFromPeers = set(values[peer] for peer in peers[field] if len(values[peer]) == 1)
        #value = re.sub('|'.join(distinctValuesFromPeers), '', values[field])
        
        #if len(value) == 1:
        #    values[field] = value
        #print(field, values[field]);print(distinctValuesFromPeers);print(re.sub('|'.join(distinctValuesFromPeers), '', values[field]));print()
        for unit in unitlist:
            for digit in '123456789':
                dplaces = [box for box in unit if digit in values[box]]
                if len(dplaces) == 1:
                    values[dplaces[0]] = digit
    return values