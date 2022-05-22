from random import shuffle

MINE = -1
TILE = 0
# TODO додати можливість обирати розмір поля - словник з розмірами полів (S, M, L, XL)
field_size = 8
mines = 8


def create_field(mines=mines, size=field_size):
    field = [MINE for m in range(mines)] + [TILE for t in range(size ** 2 - mines)]
    shuffle(field)
    x_field = ['X' for i in range(size ** 2)]
    return field, x_field


solved_field, current_field = create_field()


def find_neighbor_indexes(index):
    if index == 0:  # left-up
        neighbors = [index + 1, index + 9, index + 8]
    elif index == field_size - 1:  # right-up
        neighbors = [index - 1, index + 8, index + 7]
    elif index == field_size * (field_size - 1):  # left-down
        neighbors = [index - 8, index - 7, index + 1]
    elif index == field_size ** 2 - 1:  # right-down
        neighbors = [index - 9, index - 8, index - 1]
    elif 0 < index < field_size - 1:  # up
        neighbors = [index - 1, index + 1, index + 7, index + 8, index + 9]
    elif index % field_size == 0:  # left
        neighbors = [index - 8, index - 7, index + 1, index + 8, index + 9]
    elif (index + 1) % field_size == 0:  # right
        neighbors = [index - 9, index - 8, index - 1, index + 7, index + 8]
    elif field_size * (field_size - 1) < index < field_size ** 2 - 1:  # down
        neighbors = [index - 9, index - 8, index - 7, index - 1, index + 1]
    else:  # center
        neighbors = [index - 9, index - 8, index - 7, index - 1, index + 9, index + 8, index + 7, index + 1]
    return neighbors


def mark_mines(field=solved_field):
    for i in range(field_size ** 2):
        if field[i] != -1:
            neighbors = find_neighbor_indexes(i)
            field[i] = [solved_field[i] for i in neighbors].count(-1)
    return field


solved_field = mark_mines()


def print_solved_field(field=solved_field, size=field_size):
    for i in range(0, size**2, size):
        print(*field[i:i + size])
    print('\n')


# print_solved_field()


def print_current_field(field=current_field, size=field_size):
    for i in range(0, size ** 2, size):
        print(*field[i:i + size])
    print('\n')


print_current_field()


def play():
    print('Horizontal Vertical')
    while True:
        column, raw = input('Make your move: ').split()
        column = int(column) - 1
        raw = int(raw) - 1
        shoot = column + raw * field_size
        try:
            current_field[shoot] = solved_field[shoot]
        except IndexError:
            print('You are out of field. Make another move')
            continue
        if solved_field[shoot] == -1:  # GAME OVER
            print('BAAAAM. You lost!')
            break
        else:
            update_field(shoot)
            print_current_field()


def update_field(target, field=solved_field):
    if field[target] > 0:
        return current_field
    else:  # when 0
        neighbors = find_neighbor_indexes(target)
        for tile in neighbors:
            if solved_field[tile] != -1 and solved_field[tile] != current_field[tile]:
                if solved_field[tile] == 0:
                    current_field[tile] = solved_field[tile]
                    update_field(target=tile)
                else:
                    current_field[tile] = solved_field[tile]
        return current_field


if __name__ == '__main__':
    play()
