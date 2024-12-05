from my_advent.day1 import compare_list_distance as a
from my_advent.day1 import compare_list_similarity as b

EXAMPLE_INPUT = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]


def test_example_a():
    example_result = 11
    assert a(EXAMPLE_INPUT) == example_result


def test_example_b():
    example_result = 31
    assert b(EXAMPLE_INPUT) == example_result
