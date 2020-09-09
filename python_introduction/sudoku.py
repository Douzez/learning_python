# Function that prints the board as a matrix

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def print_board(the_board):
    print('    0 1 2   3 4 5   6 7 8')
    line = '  ' + '-' * 25
    for r in range(len(board)):
        if r % 3 == 0:
            print(line)
        row_to_print = str(r)
        for c in range(len(the_board[0])):
            if c % 3 == 0:
                row_to_print += " |"
            row_to_print += ' ' + str(the_board[r][c]) if the_board[r][c] > 0 else '  '
        row_to_print += ' |'
        print(row_to_print)
    print(line)


print_board(board)

"""
Find the first empty cell, read the board from left to right and top to down.
The output of that function should be at list of size 2.
1st element is the row number, 2nd element is the col number
"""
def find_zero(the_board):
    # return [0, 2] ==> row, col
    for row in range(len(the_board)):
        for col in range(len(the_board[row])):
            if the_board[row][col] == 0:
                return [row, col]
    return []

print(find_zero(board))


"""
Valid Placement. it takes the board, row-col positions, and a value (1-9) -> (board, 0, 2, 7)
and determines if it's legal to place that number on the cell.

* Check the entire row to see if there's a number that matches the value. if there is, 
    do not place that value on the cell.
* Do the same as above for the column
* Do the same with the 3x3 grid.

The output should simply be a boolean value.
"""

def is_valid(the_board, the_row, the_col, value):
    # Validate Value not in Row
    if value in the_board[the_row]:
        return False

    # Validate Value not in Column
    for row in the_board:
        if value == row[the_col]:
            return False

    # Validate Value in 3x3 Grid
    row = the_row // 3
    col = the_col // 3
    for r in range(3):
        for c in range(3):
            if the_board[(3 * row) + r][(3 * col) + c] == value:
                return False

    return True

row_col = find_zero(board)
print(is_valid(board, row_col[0], row_col[1], 7))  # False  7 is in the row
print(is_valid(board, 7, 5, 9))                    # False  8 is in the column
print(is_valid(board, row_col[0], row_col[1], 9))  # False  9 is in the 3x3 Grid

print(is_valid(board, 8, 6, 1))                    # True   1 is not in the row nor col nor 3x3 grid
print(is_valid(board, 8, 6, 5))                    # False  5 is in the row nor col nor 3x3 grid
print(is_valid(board, row_col[0], row_col[1], 4))  # True   4 is not in the row nor col nor 3x3 grid 
