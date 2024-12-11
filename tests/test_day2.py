from my_advent.day2 import a, b


EXAMPLE_INPUT = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]
EXAMPLE_RESULT_A = 2
EXAMPLE_RESULT_B = 0


def test_example_a():
    assert a(EXAMPLE_INPUT) == EXAMPLE_RESULT_A


def test_example_b():
    assert b(EXAMPLE_INPUT) == EXAMPLE_RESULT_B
