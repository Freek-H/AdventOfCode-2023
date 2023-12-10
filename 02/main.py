from pathlib import Path

CURRENT_WORKING_DIRECTORY = Path(__file__).parent


def read_file():
    with open(CURRENT_WORKING_DIRECTORY / "input.txt") as input_file:
        data = (
            input_file.read().rstrip("\n").split("\n")
        )  # removing a final newline if it exists as to allow the split to not produce a final empty string element
    return data


def problem_1(data):
    limits = dict(red=12, green=13, blue=14)

    counter = 0
    for one_game_name, one_game_sets in data.items():
        valid = True
        for one_set in one_game_sets:
            for colour, limit in limits.items():
                if colour in one_set and one_set[colour] > limit:
                    valid = False
                    break
        if valid:
            counter += int(one_game_name.split()[-1])

    return counter


def problem_2(data):
    pass


def main():
    raw_data = read_file()

    data = {}
    for line in raw_data:
        game_name = line.split(":")[0]
        sets = [one_set.strip() for one_set in line.split(":")[-1].split(";")]
        dict_sets = []
        for one_set in sets:
            one_dict_set = {}
            for one_colour in one_set.split(", "):
                colour = one_colour.split()[-1]
                amount = int(one_colour.split()[0])
                one_dict_set[colour] = amount
            dict_sets.append(one_dict_set)

        data[game_name] = dict_sets

    solution_1 = problem_1(data)
    print(f"Solution to problem 1: {solution_1}")

    solution_2 = problem_2(data)
    print(f"Solution to problem 2: {solution_2}")


if __name__ == "__main__":
    main()
