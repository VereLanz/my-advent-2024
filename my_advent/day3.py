from pathlib import Path
import re

from my_advent import get_todays_puzzle


def add_corrupt_mul_statements(inputs: list[str]) -> int:
    mul_command_pattern = r"mul\(([\d]+),([\d]+)\)"
    mul_commands = re.findall(mul_command_pattern, "".join(inputs))
    return sum([int(a) * int(b) for a, b in mul_commands])


def add_enabled_mul_statements(inputs: list[str]) -> int:
    whole_input = "".join(inputs)
    # removing all the text between don't() and do()
    # start is a do() section
    all_do = whole_input.split("do()")
    only_do = [parts.split("don't()")[0] for parts in all_do]

    mul_command_pattern = r"mul\(([\d]+),([\d]+)\)"
    mul_commands = re.findall(mul_command_pattern, "".join(only_do))
    return sum([int(a) * int(b) for a, b in mul_commands])


# only for least effort template working each day
a = add_corrupt_mul_statements
b = add_enabled_mul_statements


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
