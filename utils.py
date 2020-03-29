rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)
#boxes : A1,A2,....I8,I9  (len(boxes) = 81)

row_units = [cross(r, cols) for r in rows]
#[B1,B2,B3,B4,...B9], [C1,C2,...C9].....
column_units = [cross(rows, c) for c in cols]
#[A1,B1,C1...], [A2,B2,...].....
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
#[A1,A2,A3,B1,B2,B3,C1,C2,C3], .....
unitlist = row_units + column_units + square_units
#complete rows, columns, and 3x3 squares : UNITS
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
#A1 : [if A1 in rows], [if A1 in columns], [if A1 in 3x3 squares]
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
#{'A1': {'A5', 'A7', 'C1', 'A9', 'E1', 'C3', 'A2' ......}, 'A2': {.....
#every element: its peers

dioganal_units_right = [str(i[0]+i[1]) for i in list(zip(rows, cols))]
dioganal_units_left = [str(i[0]+i[1]) for i in list(zip(rows, cols[::-1]))]
dioganal = list(set(dioganal_units_right + dioganal_units_left))


# TODO: Update the unit list to add the new diagonal units
unitlist = unitlist + [dioganal_units_left] + [dioganal_units_left]
def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

