from my_advent.day6 import a, b


EXAMPLE_INPUT = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]
EXAMPLE_RESULT_A = 41
EXAMPLE_RESULT_B = 0


def test_example_a():
    assert a(EXAMPLE_INPUT) == EXAMPLE_RESULT_A


def test_example_b():
    assert b(EXAMPLE_INPUT) == EXAMPLE_RESULT_B
