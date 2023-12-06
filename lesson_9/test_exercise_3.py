import pytest
from lesson_9 import add_three_numbers

# solution 1
def test_solution_1_standard():
    assert add_three_numbers(3, 3, 3) == 9

def test_solution_1_positive():
    assert add_three_numbers(-3, 4, 0) == 1

def test_solution_1_negative():
    assert add_three_numbers(-3, -1, -4) == -8

# solution 2
@pytest.mark.parametrize("numb_1, numb_2, numb_3, result", [
    pytest.param(3, 3, 3, 9, id="standard"),
    pytest.param(-3, 4, 0, 1, id="negative and positive"),
    pytest.param(-3, -1, -4, -8, id="tree negative")])
def test_solution_2(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result

# solution 3
list_test = [(3, 3, 3, 9), (-3, 4, 0, 1), (-3, -1, -4, -8)]

@pytest.mark.parametrize("numb_1, numb_2, numb_3, result", list_test)
def test_solution_3(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result

