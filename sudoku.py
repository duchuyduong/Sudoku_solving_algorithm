grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]
def puzzle(a):
    for x in range(9):
        for y in range(9):
            print(a[x][y], end=" ")
        print()

def solver(grid, row, col, i):
    for col_num in range(9):
        if grid[row][col_num] == i:
            return False
    for row_num in range(9):
        if grid[row_num][col] == i:
            return False
    row_bracket = row - row % 3
    col_bracket = col - col % 3
    for n in range(3):
        for m in range(3):
            if grid[n + row_bracket][m + col_bracket] == i:
                return False
    return True

def checking(grid, row, col):
    if row == 8 and col == 8:
        return True
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        if col != 8:
            return checking(grid, row, col + 1)
        else:
            return checking(grid, row + 1, 0)
    for i in range(1, 10):
        if solver(grid, row, col, i):
            grid[row][col] = i
            if checking(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

if checking(grid, 0, 0):
    puzzle(grid)
else:
    print('no result')
