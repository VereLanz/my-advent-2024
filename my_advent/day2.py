from pathlib import Path

from my_advent import get_todays_puzzle


def check_report_safety_level(inputs: list[str]) -> int:
    reports = [[int(l) for l in line.split()] for line in inputs]
    safe_amount = 0
    for report in reports:
        if sorted(report) == report or sorted(report, reverse=True) == report:
            increments = [abs(report[i] - report[i+1]) for i in range(len(report) - 1)]
            if all(inc <= 3 and inc > 0 for inc in increments):
                safe_amount += 1
    return safe_amount


def check_dampened_safety_level(inputs: list[str]) -> int:
    reports = [[int(l) for l in line.split()] for line in inputs]
    safe_amount = 0
    for report in reports:
        if sorted(report) == report or sorted(report, reverse=True) == report:
            if has_safe_increments(report):
                safe_amount += 1
            elif safe_with_exception(report):
                safe_amount += 1
        elif sorted_and_safe_with_exception(report):
            safe_amount += 1

    return safe_amount


def has_safe_increments(numbers: list[int]) -> bool:
    # increments between 1 and 3 check; no values removed here
    increments = [abs(numbers[i] - numbers[i+1]) for i in range(len(numbers) - 1)]
    return all(inc <= 3 and inc > 0 for inc in increments)
    

def safe_with_exception(numbers: list[int]) -> bool:
    # is already sorted, but not incrementing correctly; can still remove one
    for i in range(len(numbers)):
        new_numbers = numbers.copy()
        new_numbers.pop(i)
        if has_safe_increments(new_numbers):
            return True
    return False


def sorted_and_safe_with_exception(numbers: list[int]) -> bool:
    # not sorted; can still remove one and check increments then
    for i in range(len(numbers)):
        new_numbers = numbers.copy()
        new_numbers.pop(i)
        if (sorted(new_numbers) != new_numbers and 
            sorted(new_numbers, reverse=True) != new_numbers):
            continue
        if has_safe_increments(new_numbers):
            # both checks passed with 1 removed
            return True
    return False


# only for least effort template working each day
a = check_report_safety_level
b = check_dampened_safety_level


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
