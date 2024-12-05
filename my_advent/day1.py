from pathlib import Path

import numpy as np

from my_advent import get_todays_puzzle


def compare_list_distance(inputs: list[str]) -> int:
    left_list = [int(i.split()[0]) for i in inputs]
    right_list = [int(i.split()[-1]) for i in inputs]
    sum = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        sum += abs(left - right)
    return sum


def compare_list_similarity(inputs: list[str]) -> int:
    left_list = [int(i.split()[0]) for i in inputs]
    right_list = np.array([int(i.split()[-1]) for i in inputs])
    sum = 0
    for left_value in left_list:
        occurence = len(np.where(right_list == left_value)[0])
        sum += left_value * occurence
    return sum


# only for least effort template working each day
a = compare_list_distance
b = compare_list_similarity


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
