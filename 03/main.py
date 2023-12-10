from pathlib import Path

CURRENT_WORKING_DIRECTORY = Path(__file__).parent


def read_file():
    with open(CURRENT_WORKING_DIRECTORY / "input.txt") as input_file:
        data = (
            input_file.read().rstrip("\n").split("\n")
        )  # removing a final newline if it exists as to allow the split to not produce a final empty string element
    return data


def is_symbol(character):
    non_symbols = tuple(str(number) for number in range(10)) + (".",)

    return character not in non_symbols


def has_symbol_neighbour(matrix, row_number, column_number):
    total_number_of_rows = len(matrix)
    total_number_of_columns = len(matrix[row_number])

    rows_to_check = range(
        max(row_number - 1, 0), min(row_number + 1, total_number_of_rows - 1) + 1
    )
    columns_to_check = range(
        max(column_number - 1, 0),
        min(column_number + 1, total_number_of_columns - 1) + 1,
    )

    at_least_one_symbol_neighbour = False
    for row in rows_to_check:
        for column in columns_to_check:
            if row == row_number and column == column_number:
                continue
            if is_symbol(matrix[row][column]):
                at_least_one_symbol_neighbour = True

    return at_least_one_symbol_neighbour


def problem_1(data):
    current_number_string = ""
    has_symbol_neighbour_ = False
    numbers = []
    for row_number in range(len(data)):
        for column_number, character in enumerate(data[row_number]):
            if not character.isdigit() and current_number_string:
                numbers.append((int(current_number_string), has_symbol_neighbour_))
                current_number_string = ""
                has_symbol_neighbour_ = False
                continue
            if character.isdigit():
                current_number_string += character
                has_symbol_neighbour_ |= has_symbol_neighbour(
                    data, row_number, column_number
                )

    answer = sum(
        part_number * is_part_number for part_number, is_part_number in numbers
    )
    return answer


def problem_2(data):
    pass


def main():
    data = read_file()

    answer_1 = problem_1(data)
    print(f"Solution to problem 1: {answer_1}")

    answer_2 = problem_2(data)
    print(f"Solution to problem 2: {answer_2}")


if __name__ == "__main__":
    main()
