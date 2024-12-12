from pathlib import Path

from my_advent import get_todays_puzzle


def find_all_XMAS(inputs: list[str]) -> int:
    search_word = "XMAS"
    xmas_count = 0
    xmas_count += find_horizontal_words(inputs, search_word)
    xmas_count += find_vertical_words(inputs, search_word)
    xmas_count += find_diagonal_words(inputs, search_word)
    return xmas_count


def find_horizontal_words(field: list[str], search_word: str) -> int:
    find_count = 0
    for line in field:
        if search_word in line or search_word in line[::-1]:
            find_count += 1
    return find_count


def find_vertical_words(field: list[str], search_word: str) -> int:
    find_count = 0
    # create letter rows to search in instead of lines
    for i in range(len(field[0])):
        row = "".join([line[i] for line in field])
        if search_word in row or search_word in row[::-1]:
            find_count += 1
    return find_count


def find_diagonal_words(field: list[str], search_word: str) -> int:
    find_count = 0
    # create diagonals to search in instead of lines or rows
    diagonals = []
    for i in range(len(field)):  # line index
        for j in range(i+1):  # row index


    
    
    diagonal = "".join([line[i] for line in field])
    if search_word in row or search_word in row[::-1]:
        find_count += 1
    return find_count


def b(inputs: list[str]) -> int:
    return len(inputs)


# only for least effort template working each day
a = find_all_XMAS
b = b


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
