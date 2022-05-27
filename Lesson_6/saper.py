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
    while True:
        try:
            size = input('Choose the field size: ')
            print('Initializing field {0}*{0}. Number of mines - {0}'.format(SIZES[size]), end='\n\n')
            break
        except KeyError:
            print("I don't have this field size. Please choose one of this: S, M, L, XL")
            continue
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
        neighbors = [index - s, index - s+1, index + 1]
    elif index == s ** 2 - 1:  # right-down
        neighbors = [index - s-1, index - s, index - 1]
    elif 0 < index < s - 1:  # up
        neighbors = [index - 1, index + 1, index + s-1, index + s, index + s+1]
    elif index % s == 0:  # left
        neighbors = [index - s, index - s+1, index + 1, index + s, index + s+1]
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


def shooted_tile(move):
    try:
        column, raw = move.split()
        column = int(column) - 1
        raw = int(raw) - 1
    except ValueError:
        print('Please enter two numbers from 1 to {}'.format(field_size))
        return True
    shoot = column + raw * field_size
    if shoot < 0:
        print('Please enter two numbers from 1 to {}'.format(field_size))
        return True
    try:
        current_field[shoot] = solved_field[shoot]
    except IndexError:
        print('You are out of field. Make another move')
        return True
    return shoot


def perform_move(move):

    if move == 'm':
        while True:
            move = input('What tile do you want to mark? ')
            shoot = shooted_tile(move)
            if isinstance(shoot, bool):
                continue
            break
        update_field(target=shoot, marking=True)
        print_current_field()
        return True

    if move == 'e':  # exit from the game
        print('It was a great game! Good bye =)')
        return False

    shoot = shooted_tile(move)
    if isinstance(shoot, bool):
        return True

    if solved_field[shoot] == -1:  # GAME OVER
        print_current_field()
        print('BAAAAM. You lost!')
        return False
    else:
        update_field(shoot)
        print_current_field()
        return True


def update_field(target, field=solved_field, marking=False):

    if marking:  # marking mode
        current_field[target] = 'M'
        return current_field

    elif field[target] > 0:  # when marked tile is shooted, I need to open only this one
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


def is_winning():
    if current_field.count('X') + current_field.count('M') == field_size:
        print('YOU WON!')
        return True
    else:
        return False


def play(game=True):
    print_current_field()
    print('Input 2 numbers divided by space. First for the column and second is for the raw.', end='\n\n')
    while game:
        move = input('Make your move: ').strip()
        game = perform_move(move)
        if is_winning():
            break


if __name__ == '__main__':
    print_solved_field()
    play()
