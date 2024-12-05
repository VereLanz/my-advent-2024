from my_advent.day1 import  a, b

EXAMPLE_INPUT = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]
EXAMPLE_RESULT_A = 11
EXAMPLE_RESULT_B = 31


def test_example_a():
    assert a(EXAMPLE_INPUT) == EXAMPLE_RESULT_A


def test_example_b():
    assert b(EXAMPLE_INPUT) == EXAMPLE_RESULT_B
