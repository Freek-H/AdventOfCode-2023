# This file is a template containing the boiler plate code for the AOC challenges.

from pathlib import Path

CURRENT_WORKING_DIRECTORY = Path(__file__).parent


def read_file():
    with open(CURRENT_WORKING_DIRECTORY / "input.txt") as input_file:
        data = (
            input_file.read().rstrip("\n").split("\n")
        )  # removing a final newline if it exists as to allow the split to not produce a final empty string element
    return data


def problem_1(data):
    pass


def problem_2(data):
    pass


def main():
    data = read_file()

    solution_1 = problem_1(data)
    print(f"Solution to problem 1: {solution_1}")

    solution_2 = problem_2(data)
    print(f"Solution to problem 2: {solution_2}")


if __name__ == "__main__":
    main()
