from pathlib import Path

from my_advent import get_todays_puzzle, MyPuzzle


def compare_list_distance(inputs: list[str]) -> int:
    left_list = [int(i.split()[0]) for i in inputs]
    right_list = [int(i.split()[-1]) for i in inputs]
    sum = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        sum += abs(left - right)
    return sum


def b(inputs: list[str]) -> int:
    return 0


def solve_a(puzzle: MyPuzzle):
    answer_a = compare_list_distance(puzzle.input_lines)
    puzzle.submit_a(answer_a)


def solve_b(puzzle: MyPuzzle):
    answer_b = b(puzzle.input_lines)
    puzzle.submit_b(answer_b)


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)
    solve_a(my_puzzle)
    # solve_b(my_puzzle)
