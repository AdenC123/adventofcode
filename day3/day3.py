import re
import itertools as it


# MAIN
def part1(lines) -> int:
    return sum(it.starmap(lambda a, b: int(a) * int(b), re.findall(r'mul\((\d+),(\d+)\)', lines)))


def part2(lines) -> int:
    matches = re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|(don)\'t\(\)', lines)
    mul = True
    total = 0
    for (a, b, do, don) in matches:
        if do:
            mul = True
        if don:
            mul = False
        if a and mul:
            total += int(a) * int(b)
    return total

def main():
    with open("test.txt") as f:
        lines = f.read()
        print("Part 1 Test: " + str(part1(lines[:])))
        print("Part 2 Test: " + str(part2(lines[:])))
    with open("input.txt") as f:
        lines = f.read()
        print("Part 1 Input: " + str(part1(lines[:])))
        print("Part 2 Input: " + str(part2(lines[:])))


if __name__ == '__main__':
    main()
