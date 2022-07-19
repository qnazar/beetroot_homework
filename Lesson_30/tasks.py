"""This code implements all things at ones. It can work with simple math expressions, digits with boolean operators
(but in 'Pythonic way'), regular boolean expressions. Don't forget to put your expressions into (), even 'not'.
For example '(7 and (not 5))' """


import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = parse_input_str(math_exp)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i == 'not':
            current_tree = stack.pop()
            current_tree.left_child = None
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i in ['+', '-', '*', '/', 'and', 'or']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')', 'and', 'or', 'not']:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                try:
                    if i == 'True':
                        current_tree.set_root_val(True)
                    elif i == 'False':
                        current_tree.set_root_val(False)
                    parent = stack.pop()
                    current_tree = parent
                except ValueError:
                    raise ValueError("token '{}' is not a valid integer or boolean".format(i))

    return tree


def parse_input_str(math_exp: str) -> list:
    """Helper function to parse input expression without spaces"""
    token_list = []
    dig_memory = ''
    alpha_memory = ''
    for char in math_exp:
        if char.isspace():
            if alpha_memory:
                token_list.append(alpha_memory)
                alpha_memory = ''
            if dig_memory:
                token_list.append(dig_memory)
                dig_memory = ''
            continue
        if char.isdigit():
            if alpha_memory:
                token_list.append(alpha_memory)
                alpha_memory = ''
            dig_memory += char
        elif char.isalpha():
            if dig_memory:
                token_list.append(dig_memory)
                dig_memory = ''
            alpha_memory += char
        else:
            if alpha_memory:
                token_list.append(alpha_memory)
                alpha_memory = ''
            if dig_memory:
                token_list.append(dig_memory)
                dig_memory = ''
            token_list.append(char)

    return token_list


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, 'and': operator.and_,
                'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    elif not left_c and right_c:
        fn = operates['not']
        return fn(evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    """Function is_leaf() defined in the oop_tree.py"""
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child()) if not tree.is_leaf() else print_exp(tree.get_left_child())
        s_val = s_val + ' ' + str(tree.get_root_val()) if s_val else s_val + str(tree.get_root_val())
        s_val = s_val + ' ' + print_exp(tree.get_right_child()) + ')' \
            if not tree.is_leaf() else s_val + print_exp(tree.get_right_child())
    return s_val


if __name__ == "__main__":
    bpt: BinaryTree = build_parse_tree('((5 and 4) or (not 5))')
    print(evaluate(bpt))
    print(print_exp(bpt))

    bpt2 = build_parse_tree('((True or False) and (not False))')
    print(evaluate(bpt2))
    print(print_exp(bpt2))




