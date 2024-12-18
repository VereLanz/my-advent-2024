from pathlib import Path

from my_advent import get_todays_puzzle


def a(inputs: list[str]) -> int:
    return len(inputs)


def b(inputs: list[str]) -> int:
    return len(inputs)


# only for least effort template working each day
a = a
b = b


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
