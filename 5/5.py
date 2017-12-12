def get_input():
    f = open("input", "r")
    ret = f.read().split('\n')
    if ret[-1] == '':
        ret.pop()
    ret = map(int, ret)
    return ret

def part1(lst):
    place = 0
    steps = 0
    while place < len(lst) and place >= 0:
        new = place+lst[place]
        lst[place]+=1;
        place = new;
        steps+=1;
    return steps

def part2(lst):
    place = 0
    steps = 0
    while place < len(lst) and place >= 0:
        offset = lst[place]
        new = place+offset
        if offset >= 3:
            lst[place]-=2
        lst[place]+=1;
        place = new;
        steps+=1;
    return steps

print "part one answer"
print part1(get_input())
print "part two answer"
print part2(get_input())
