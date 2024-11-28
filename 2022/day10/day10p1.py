prog = []
check = (20, 60, 100, 140, 180, 220)

with open('input.txt') as f:
    for line in f:
        prog.append(line.strip())

cycle = 0
x = 1
wait = 0
hold_val = 0
sum = 0


while prog or hold_val:
    cycle += 1
    # print(f'During cycle {cycle} x is {x}')
    if cycle in check:
        sum += x * cycle

    if hold_val:
        x += hold_val
        hold_val = 0
    else:
        ins = prog.pop(0)
        if ins == 'noop':
            pass
        else:
            hold_val = int(ins.split()[1])
            wait = 1

    # print(f'After cycle {cycle} x is {x}')
print(sum)