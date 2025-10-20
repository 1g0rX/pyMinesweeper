# função para formar o mapa

from random import randint

minesweeper_map = list()
minesweeper_map_helper = list()
marked_positions = dict()
count = 0
bombs_count = 0


def create_map(x, y):
    """Function that create a blank map"""

    for i in range(x):
        # add an empty list in the map and a copy
        line_map = []
        line_map_copy = []
        for j in range(y):
            line_map.append(' ') # add a space in each list
            line_map_copy.append(' ')
        minesweeper_map.append(line_map)
        minesweeper_map_helper.append(line_map_copy)
    

def input_mines(x, y, mines):
    """Function that receives the number of lines, columns and also the number os mines and put the bombs in randoms places"""
    for i in range(mines):
        # randint includes the first and by the last element given
        op_x = randint(0, x - 1)
        op_y = randint(0, y - 1)
        if minesweeper_map[op_x][op_y] == ' ': # if there is not a bomb in these coordinates, put a bomb there
            minesweeper_map[op_x][op_y] = '*'
    print('Bombs allocated!')
            
def mark_as_mine(line, column):
    for coordinates in marked_positions.values(): # verify if these coordinates are marked as possible mines
        if line == coordinates[0] and column == coordinates[1]:
            print(f'Position {line + 1}/{column + 1} already marked as possible mine.')
            return count
    
    minesweeper_map_helper[line][column] = 'M'
    marked_positions[count] = [line, column]
    return count + 1

def open_position(line, column):
    if minesweeper_map[line][column] == '*':
        print("BOOOOOMBAAAAA!!!!")
        print("Você morreu!!")
        return False
    else: 
        # change the map helper to show the number of mines nearby
        total_mines = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # ignore the just opened position
                if i == 0 and j == 0: 
                    continue
                # check if it is in the map's limit
                if (line + i) < 0 or (line + i) >= len(minesweeper_map) or (column + j) < 0 or (column + j) >= len(minesweeper_map[0]):
                    continue
                
                elif minesweeper_map[line + i][column + j] == '*':
                    total_mines = total_mines + 1
        minesweeper_map_helper[line][column] = str(total_mines)
        return True

def check_game_status():
    bombs_count_total = 0
    for i in range(len(minesweeper_map)):
        for j in range(len(minesweeper_map[0])):
            if minesweeper_map[i][j] == '*' and minesweeper_map_helper[i][j] == 'M':
                bombs_count_total = bombs_count_total + 1
    return bombs_count_total
    
def show_map():
    for i in range(len(minesweeper_map_helper)):
        print('|', end='')
        for j in range(len(minesweeper_map_helper[0])):
            print(minesweeper_map_helper[i][j], end='')
        print('|')



# Begin of the program logic
number_line = -1
number_column = -1

while number_line < 3 or number_line > 10:
    number_line = int(input("Number of lines (min 3 and max 10): "))

while number_column < 3 or number_column > 10:
    number_column = int(input("Number of columns (min 3 and max 10): "))

create_map(number_line, number_column)
number_mines = int()
while True:
    number_mines = int(input('Number of mines: '))
    if number_mines >= (number_column * number_line):
        print('The number of mines cannot be higher than the number of tiles')
    else:
        break

input_mines(number_line, number_column, number_mines)

while True:
    show_map()
    print('\n')
    print("1. Mark as mine")
    print("2. Open coordinates")
    print("0. Exit")
    op = int(input("Option: "))
    match op:
        case 0:
            break
        
        case 1: 
            print('Mark as mine: ')
            line = int(input('\t line: '))
            column = int(input('\tColumn: '))

            count = mark_as_mine(line - 1, column - 1)
        
        case 2:
            print('Open coordinates: ')
            line = int(input('\tline: '))
            column = int(input('\tColumn: '))

            if not open_position(line - 1, column - 1):
                break


    bombs_count = check_game_status()
    if bombs_count == number_mines:
        print("Well done")
        show_map()
        break


