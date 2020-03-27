from utils import *
from itertools import chain, repeat

import sys
#grid = sys.argv[1]
# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """

    d = dict(zip(boxes, chain(list(grid), repeat(None))))
    return d

print(display(grid_values(grid)))