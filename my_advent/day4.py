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
        find_count += line.count(search_word)
        find_count += line[::-1].count(search_word)
    return find_count


def find_vertical_words(field: list[str], search_word: str) -> int:
    find_count = 0
    # create letter rows to search in instead of lines
    for i in range(len(field[0])):
        row = "".join([line[i] for line in field])
        find_count += row.count(search_word)
        find_count += row[::-1].count(search_word)
    return find_count


def find_diagonal_words(field: list[str], search_word: str) -> int:
    # create diagonals to search in instead of lines or rows
    diagonals = []
    
    # from lower left to upper right
    for i in range(len(field) + len(field[0]) - 1):
        diagonal = []
        for j in range(i+1):
            try:
                # some indices will be out of range due to the nature of this walk
                diagonal.append(field[i-j][j])
            except IndexError:
                pass
        diagonals.append("".join(diagonal))

    # from upper left to lower right
    longest_dim = max(len(field), len(field[0]))
    for offset in range(longest_dim):
        diagonal_up = []
        diagonal_down = []
        for i in range(offset, longest_dim):
            try:
                # some indices will be out of range due to the nature of this walk
                diagonal_up.append(field[i][i-offset])
                diagonal_down.append(field[i-offset][i])
            except IndexError:
                pass
        diagonals.append("".join(diagonal_up))
        if offset == 0:
            # in this one case both diagonals are the same, don't count double!
            continue
        diagonals.append("".join(diagonal_down))
    
    find_count = 0
    for diagonal in diagonals:
        find_count += diagonal.count(search_word)
        find_count += diagonal[::-1].count(search_word)
    return find_count


def find_actual_X_MAS(inputs: list[str]) -> int:
    search_word = "MAS"
    x_mas_count = 0
    # search diagonally for every 3x3 segment
    for i in range(len(inputs) - 2):
        for j in range(len(inputs[0]) - 2):
            search_lines = inputs[i : i+3]
            search_field = [
                [line[col] for col in range(j, j+3)] for line in search_lines
            ]
            # 2 MAS are found diagonally in 3x3 only if in an X shape
            if find_diagonal_words(search_field, search_word) == 2:
                x_mas_count += 1
    return x_mas_count


# only for least effort template working each day
a = find_all_XMAS
b = find_actual_X_MAS


if __name__ == "__main__":
    # assumes the filename is always "day{day_nr}"
    day_nr = int(Path(__file__).stem[3:])
    my_puzzle = get_todays_puzzle(day_nr)

    # my_puzzle.submit_a(a(my_puzzle.input_lines))
    # my_puzzle.submit_b(b(my_puzzle.input_lines))
