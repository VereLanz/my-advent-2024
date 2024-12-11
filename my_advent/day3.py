from pathlib import Path
import re

from my_advent import get_todays_puzzle


def add_corrupt_mul_statements(inputs: list[str]) -> int:
    mul_command_pattern = r"mul\(([\d]+),([\d]+)\)"
    mul_commands = re.findall(mul_command_pattern, "".join(inputs))
    return sum([int(a) * int(b) for a, b in mul_commands])


def b(inputs: list[str]) -> int:
    return len(inputs)


# only for least effort template working each day
a = add_corrupt_mul_statements
b = b


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
