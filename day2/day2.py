from itertools import pairwise


def safe(report):
    return all(1 <= a-b <= 3 for a, b in pairwise(report)) or all(1 <= b-a <= 3 for a, b in pairwise(report))


# MAIN
def part1(lines) -> int:
    reports = [list(map(int, line.split())) for line in lines]
    return sum(safe(r) for r in reports)            


def part2(lines) -> int:
    reports = [list(map(int, line.split())) for line in lines]
    return sum(safe(r) or any(safe(r[:i]+r[i+1:]) for i in range(len(r))) for r in reports)


def main():
    with open("test.txt") as f:
        lines = f.readlines()
        print("Part 1 Test: " + str(part1(lines[:])))
        print("Part 2 Test: " + str(part2(lines[:])))
    with open("input.txt") as f:
        lines = f.readlines()
        print("Part 1 Input: " + str(part1(lines[:])))
        print("Part 2 Input: " + str(part2(lines[:])))


if __name__ == '__main__':
    main()
