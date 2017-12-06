def get_input():
    f = open("input", "r")
    return f.read().split()[0]

def part1(inp):
    length = len(inp)
    inp += inp[0]
    s = 0
    for place in range(length):
        if inp[place] == inp[place+1]:
            s += int(inp[place])
    return s

def part2(inp):
    look = len(inp)/2
    inp += inp
    s = 0
    for place in range(len(inp)/2):
        if inp[place] == inp[place+look]:
            s += int(inp[place])
    return s

inp = get_input()
print "part one answer"
print part1(inp)
print "part two answer"
print part2(inp)
