myTree = ['a',  # root
          ['b',  # left subtree
           ['d', [], []],
           ['e', [], []]],
          ['c',  # right subtree
           ['f', [], []],
           []]
          ]


def BinaryTree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def find_max(root, max_l=[]):
    max_l.append(get_root_val(root))
    if get_left_child(root):
        find_max(get_left_child(root), max_l)
    if get_right_child(root):
        find_max(get_right_child(root), max_l)
    print(max_l)
    return max(max_l)




if __name__ == "__main__":
    tr = BinaryTree(3)
    insert_left(tr, 4)
    insert_left(tr, 5)
    insert_right(tr, 6)
    insert_right(tr, 7)
    left = get_left_child(tr)
    print(left)

    set_root_val(left, 9)
    print(tr)
    insert_left(left, 11)
    print(tr)
    print(get_right_child(get_right_child(tr)))
    print(find_max(tr))
