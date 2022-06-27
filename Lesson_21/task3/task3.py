from Lesson_21.task1.Open import Open
import pytest


def sort_data(file_obj):
    data = file_obj.read()
    data = sorted(data.split('\n'))
    return data


@pytest.fixture
def list_of_colors():
    with Open('colors.txt') as f:
        return sort_data(f)


def test_sort_data(list_of_colors):
    assert list_of_colors == ['black', 'blue', 'pink', 'red', 'white']


