


# MAIN
def part1(lines) -> int:
    l1 = sorted(int(line.split()[0]) for line in lines)
    l2 = sorted(int(line.split()[1]) for line in lines)
    return sum(abs(x - y) for x, y in zip(l1, l2))


def part2(lines) -> int:
    l1 = sorted(int(line.split()[0]) for line in lines)
    l2 = sorted(int(line.split()[1]) for line in lines)
    return sum(x * l2.count(x) for x in l1)


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        # print("Part 1 Test: " + str(part1(lines[:])))
        print("Part 2 Test: " + str(part2(lines[:])))
    with open("input.txt") as f:
        lines = f.readlines()
        # print("Part 1 Input: " + str(part1(lines[:])))
        print("Part 2 Input: " + str(part2(lines[:])))


if __name__ == '__main__':
    main()
