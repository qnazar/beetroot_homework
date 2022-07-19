from tasks import parse_input_str, build_parse_tree, evaluate, print_exp
import pytest


def test_parse_input_str():
    # simple case
    assert parse_input_str('(5 + 4)') == ['(', '5', '+', '4', ')']
    # complicated case
    assert parse_input_str('((8+6)*(18-8))') == ['(', '(', '8', '+', '6', ')', '*', '(', '18', '-', '8', ')', ')']
    # with boolean operator
    assert parse_input_str('(10 and 2)') == ['(', '10', 'and', '2', ')']
    # with boolean operator and bool operands
    assert parse_input_str('(True or False)') == ['(', 'True', 'or', 'False', ')']
    # mixed case
    assert parse_input_str('(((4 * 2) + (6-7)) or (not True))') == \
           ['(', '(', '(', '4', '*', '2', ')', '+', '(', '6', '-', '7', ')', ')', 'or', '(', 'not', 'True', ')', ')']


@pytest.fixture
def simple_tree_with_digits():
    return build_parse_tree('(5 + 4)')


@pytest.fixture
def complex_tree_with_digits():
    return build_parse_tree('((8+6)*(18-8))')


@pytest.fixture
def tree_with_bool():
    return build_parse_tree('(10 and 2)')


@pytest.fixture
def boolean_tree():
    return build_parse_tree('(True or False)')


@pytest.fixture
def tree_with_not():
    return build_parse_tree('(not True)')


def test_evaluate(simple_tree_with_digits, complex_tree_with_digits, tree_with_bool, boolean_tree, tree_with_not):
    assert evaluate(simple_tree_with_digits) == 9
    assert evaluate(complex_tree_with_digits) == 140
    assert evaluate(tree_with_bool) == 2
    assert evaluate(boolean_tree) == True
    assert evaluate(tree_with_not) == False


def test_print_exp(simple_tree_with_digits, complex_tree_with_digits, tree_with_bool, boolean_tree, tree_with_not):
    assert print_exp(simple_tree_with_digits) == '(5 + 4)'
    assert print_exp(complex_tree_with_digits) == '((8 + 6) * (18 - 8))'
    assert print_exp(tree_with_bool) == '(10 and 2)'
    assert print_exp(boolean_tree) == '(True or False)'
    assert print_exp(tree_with_not) == '( not True)'
