def get_input():
    f = open("input", "r")
    return f.read()

def prepare_input(inp):
    inp = get_input()
    inpn = inp.split('\n')
    use = []
    for line in inpn:
        use.append(line.split('\t'))
    use.pop()
    for line in range(len(use)):
        for val in range(len(use[line])):
            use[line][val] = int(use[line][val])
    return use

def part1(use):
    sums = 0
    for line in use:
        minval = line[0]
        maxval = line[0]
        for val in line:
            minval = min(minval, val)
            maxval = max(maxval, val)
        sums += maxval-minval
    return sums

def part2(use):
    sums = 0
    for line in use:
        for val in line:
            for div in line:
                if val != div and val % div == 0:
                    sums += val / div
    return sums

use = prepare_input(get_input())
print "part one answer"
print part1(use)
print "part two answer"
print part2(use)
