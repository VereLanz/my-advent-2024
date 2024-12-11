from my_advent.day3 import a, b


EXAMPLE_INPUT = [
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
]
EXAMPLE_INPUT_B = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
]
EXAMPLE_RESULT_A = 161
EXAMPLE_RESULT_B = 48


def test_example_a():
    assert a(EXAMPLE_INPUT) == EXAMPLE_RESULT_A


def test_example_b():
    assert b(EXAMPLE_INPUT_B) == EXAMPLE_RESULT_B
