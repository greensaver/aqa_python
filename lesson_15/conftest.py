import pytest
from lesson_15 import Calculator


@pytest.fixture(scope="class")
def fixture_calc():
    calc = Calculator()
    yield calc
