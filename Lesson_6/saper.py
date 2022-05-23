from random import shuffle
from art import text2art
print(text2art('--- Mine Sweeper ---'))
MINE = -1
TILE = 0
SIZES = {'S': 8,
         'M': 10,
         'L': 15,
         'XL': 20}


def choose_field_size():
    print('S - 8*8', 'M - 10*10', 'L - 15*15', 'XL - 20*20', sep='    ||    ')
    size = input('Choose the field size: ')
    print('Initializing field {0}*{0}. Number of mines - {0}'.format(SIZES[size]), end='\n\n')
    return SIZES[size]


field_size = mines = choose_field_size()


def create_field(mines=mines, size=field_size):
    field = [MINE for m in range(mines)] + [TILE for t in range(size ** 2 - mines)]
    shuffle(field)
    x_field = ['X' for i in range(size ** 2)]
    return field, x_field


solved_field, current_field = create_field()


def find_neighbor_indexes(index, s=field_size):
    if index == 0:  # left-up
        neighbors = [index + 1, index + s+1, index + s]
    elif index == s - 1:  # right-up
        neighbors = [index - 1, index + s, index + s-1]
    elif index == s * (s - 1):  # left-down
        neighbors = [index - s, index - s-1, index + 1]
    elif index == s ** 2 - 1:  # right-down
        neighbors = [index - s+1, index - s, index - 1]
    elif 0 < index < s - 1:  # up
        neighbors = [index - 1, index + 1, index + s-1, index + s, index + s+1]
    elif index % s == 0:  # left
        neighbors = [index - s, index - s-1, index + 1, index + s, index + s+1]
    elif (index + 1) % s == 0:  # right
        neighbors = [index - s-1, index - s, index - 1, index + s-1, index + s]
    elif s * (s - 1) < index < s ** 2 - 1:  # down
        neighbors = [index - s+1, index - s, index - s-1, index - 1, index + 1]
    else:  # center
        neighbors = [index - s+1, index - s, index - s-1, index - 1, index + s+1, index + s, index + s-1, index + 1]
    return neighbors


def mark_mines(field=solved_field):
    for i in range(field_size ** 2):
        if field[i] != -1:
            neighbors = find_neighbor_indexes(i)
            field[i] = [solved_field[i] for i in neighbors].count(-1)
    return field


solved_field = mark_mines()


# call to have a tips on the screen
def print_solved_field(field=solved_field, size=field_size):
    for i in range(0, size**2, size):
        print(*field[i:i + size])
    print('\n')


# TODO optimize printing with bigger sizes
def print_current_field(field=current_field, size=field_size):
    if size == 8:
        print(' |', *[n for n in range(1, size+1)])
        print('', *['-' for n in range(size+1)], sep='-')
        raw = 1
        for i in range(0, size ** 2, size):
            print(f'{raw}|', sep='', end=' ')
            print(*field[i:i + size])
            raw += 1
        print('\n')
    else:
        for i in range(0, size ** 2, size):
            print(*field[i:i + size])
        print('\n')


def play():
    print_current_field()
    print('Input 2 numbers with space between them. First number for the column and second is for the raw.', end='\n\n')
    while True:
        move = input('Make your move: ')
        if move == 'e':   # exit from the game
            print('It was a great game! Good bye =)')
            break
        try:
            column, raw = move.split()
            column = int(column) - 1
            raw = int(raw) - 1
        except ValueError:
            print('Please enter two numbers from 1 to {}'.format(field_size))
            continue
        shoot = column + raw * field_size
        if shoot < 0:
            print('Please enter two numbers from 1 to {}'.format(field_size))
            continue
        try:
            current_field[shoot] = solved_field[shoot]
        except IndexError:
            print('You are out of field. Make another move')
            continue
        if solved_field[shoot] == -1:  # GAME OVER
            print_current_field()
            print('BAAAAM. You lost!')
            break
        else:
            update_field(shoot)
            print_current_field()
        if current_field.count('X') == field_size:  # WIN
            print('YOU WON!')
            break


def update_field(target, field=solved_field):
    if field[target] > 0:  # when marked tile is shooted, I need to open only this one
        return current_field
    else:  # when 0 - open all zeros near this one and the nearest marked tiles
        neighbors = find_neighbor_indexes(target)
        for tile in neighbors:
            if solved_field[tile] != -1 and solved_field[tile] != current_field[tile]:
                if solved_field[tile] == 0:
                    current_field[tile] = solved_field[tile]
                    update_field(target=tile)  # recursion
                else:
                    current_field[tile] = solved_field[tile]
        return current_field


if __name__ == '__main__':
    print_solved_field()
    play()
