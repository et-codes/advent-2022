def get_input(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip())
    return data


def part_1():
    pass


def part_2():
    pass


if __name__ == "__main__":
    print("Part 1: ", part_1())
    print("Part 2: ", part_2())
