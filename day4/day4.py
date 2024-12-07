


def part1(text) -> int:
    rows = text.split()
    # cols = [''.join(t) for t in zip(*rows)]
    
    max_col = len(rows[0])
    max_row = len(rows)
    cols = ['' for _ in range(max_col)]
    fdiag = ['' for _ in range(max_row + max_col - 1)]
    bdiag = ['' for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x] += rows[y][x]
            fdiag[x+y] += rows[y][x]
            bdiag[x-y-min_bdiag] += rows[y][x]
    
    return sum(s.count('XMAS') + s.count('SAMX') for s in cols + rows + fdiag + bdiag)
    


def part2(text) -> int:
    rows = text.split()
    total = 0
    for x in range(len(rows[0]) - 2):
        for y in range(len(rows) - 2):
            fdiag = rows[y][x] + rows[y+1][x+1] + rows[y+2][x+2]
            bdiag = rows[y+2][x] + rows[y+1][x+1] + rows[y][x+2]
            if ((fdiag == 'MAS' or fdiag == 'SAM') and (bdiag == 'MAS' or bdiag == 'SAM')):
                total += 1
    return total
    
    

def main():
    with open("test.txt") as f:
        text = f.read()
        print("Part 1 Test: " + str(part1(text)))
        print("Part 2 Test: " + str(part2(text)))
    with open("input.txt") as f:
        text = f.read()
        print("Part 1 Input: " + str(part1(text)))
        print("Part 2 Input: " + str(part2(text)))


if __name__ == '__main__':
    main()
