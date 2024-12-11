from pathlib import Path

from my_advent import get_todays_puzzle


def check_report_safety_level(inputs: list[str]) -> int:
    reports = [[int(l) for l in line.split()] for line in inputs]
    safe_amount = 0
    for report in reports:
        print(report)
        if sorted(report) == report or sorted(report, reverse=True) == report:
            increments = [abs(report[i] - report[i+1]) for i in range(len(report) - 1)]
            if all(inc <= 3 and inc > 0 for inc in increments):
                safe_amount += 1
    return safe_amount


def b(inputs: list[str]) -> int:
    return len(inputs)


# only for least effort template working each day
a = check_report_safety_level
b = b


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
