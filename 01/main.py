from pathlib import Path

CURRENT_WORKING_DIRECTORY = Path(__file__).parent


def read_file():
    with open(CURRENT_WORKING_DIRECTORY / "input.txt") as input_file:
        data = (
            input_file.read().rstrip("\n").split("\n")
        )  # removing a final newline if it exists as to allow the split to not produce a final empty string element
    return data


def get_first_dictionary_key_by_value(dict_to_sort):
    return sorted(dict_to_sort, key=lambda x: dict_to_sort[x])[0]


def problem_1(data):
    numbers = []
    for line in data:
        first_number = None
        last_number = None

        for character in line:
            if character.isdigit():
                first_number = character
                break

        for character in reversed(line):
            if character.isdigit():
                last_number = character
                break

        if first_number is None or last_number is None:
            raise ValueError("No solution has been programmed for this edge case yet.")

        numbers.append(int(first_number + last_number))

    return sum(numbers)


def problem_2(data):
    number_string_list = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    number_strings = {key: value for value, key in enumerate(number_string_list, 1)}

    first_number, last_number = None, None

    numbers = []
    for line in data:
        found_numbers = {}

        string_number_indices = {}
        for one_number_string in number_strings.keys():
            if one_number_string in line:
                string_number_indices[one_number_string] = line.index(one_number_string)

        if string_number_indices:
            found_number_string = get_first_dictionary_key_by_value(
                string_number_indices
            )
            found_numbers[number_strings[found_number_string]] = string_number_indices[
                found_number_string
            ]

        for character in line:
            if character.isdigit():
                found_numbers[int(character)] = line.index(character)
                break

        first_number = get_first_dictionary_key_by_value(found_numbers)

        found_numbers = {}

        line = line[::-1]
        string_number_indices = {}
        for one_number_string in number_strings.keys():
            if one_number_string[::-1] in line:
                string_number_indices[one_number_string] = line.index(
                    one_number_string[::-1]
                )

        if string_number_indices:
            found_number_string = get_first_dictionary_key_by_value(
                string_number_indices
            )
            found_numbers[number_strings[found_number_string]] = string_number_indices[
                found_number_string
            ]

        for character in line:
            if character.isdigit():
                found_numbers[int(character)] = line.index(character)
                break

        last_number = get_first_dictionary_key_by_value(found_numbers)

        numbers.append(int(f"{first_number}{last_number}"))

    return sum(numbers)


def main():
    data = read_file()

    solution_1 = problem_1(data)
    print(f"Solution to problem 1: {solution_1}")

    solution_2 = problem_2(data)
    print(f"Solution to problem 2: {solution_2}")


if __name__ == "__main__":
    main()
