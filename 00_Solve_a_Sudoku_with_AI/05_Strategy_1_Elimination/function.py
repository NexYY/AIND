from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    grid_result = {}
    
    for i, value in enumerate(grid):
        if value == '.':
            grid_result[boxes[i]] = '123456789'
        else:
            grid_result[boxes[i]] = value
    
    return grid_result
    
