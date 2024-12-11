from my_advent.day4 import a, b


EXAMPLE_INPUT = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]
EXAMPLE_RESULT_A = 18
EXAMPLE_RESULT_B = 0


def test_example_a():
    # examples to find here:
    # ....XXMAS.
    # .SAMXMS...
    # ...S..A...
    # ..A.A.MS.X
    # XMASAMX.MM
    # X.....XA.A
    # S.S.S.S.SS
    # .A.A.A.A.A
    # ..M.M.M.MM
    # .X.X.XMASX
    assert a(EXAMPLE_INPUT) == EXAMPLE_RESULT_A


def test_example_b():
    assert b(EXAMPLE_INPUT) == EXAMPLE_RESULT_B
