# função para formar o mapa

from random import randint

minesweeper_map = list()
minesweeper_map_helper = list()
marked_positions = dict()

def create_map(x, y):
    """Function that create a blank map"""
    for i in range(x):
        for j in range(y):
            minesweeper_map[i][j] = ' ' # define cada espaço como espaço

def input_mines(x, y, mines):
    """Function that receives the number of lines, columns and also the number os mines and put the bombs in randoms places"""
    for i in range(mines):
        op_x = randint(0, range(x))
        op_y = randint(0, range(y))
        if minesweeper_map[op_x][op_y] == ' ': # if there is not a bomb in these coordinates, put a bomb there
            minesweeper_map[op_x][op_y] = '*'
    print('Bombs allocated!')
            
def mark_as_mine(line, column):
    for coordinates in marked_positions.values(): # verify if these coordinates are marked as possible mines
        if line == coordinates[0] or column == coordinates[1]:
            print(f'Position {line}/{column} already marked as possible mine.')
            return
    



# Begin of the program logic
number_line = 0
number_column = 0
while number_line < 3 and number_line > 10:
    number_line = int(input("Number of lines (min 3 and max 10): "))
while number_column < 3 and number_column > 10:
    number_column = int(input("Number of lines (min 3 and max 10): "))

create_map(number_line, number_column)

number_mines = input('Number of mines: ')

