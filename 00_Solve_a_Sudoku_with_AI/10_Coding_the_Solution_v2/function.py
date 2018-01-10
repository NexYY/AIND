from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!

    # Choose one of the unfilled squares with the fewest possibilities
    unfilledSquares = {box: values[box] for box in values.keys() if len(values[box]) > 1}
    fewestPossibilities = min(unfilledSquares, key=lambda k: len(unfilledSquares[k]))    

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    if len(unfilledSquares) == 0:
        return values
    
    for value in values[fewestPossibilities]:
        sudokuValues = values.copy()
        sudokuValues[fewestPossibilities] = value
        attempt = search(sudokuValues)
        
        if attempt:
            return attempt
    # If you're stuck, see the solution.py tab!

#search(values)