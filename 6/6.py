def get_input():
    f = open("input", "r")
    return map(int,f.read().split())

def array_to_string(array):
    ret = ""
    for a in array:
        ret += str(a)
    return ret

def get_max_place(array):
    ret = -1
    maxval = -1
    counter = 0
    for place in array:
        if place > maxval:
            maxval = place
            ret = counter
        counter+=1
    return ret

def redistribute(lst, place):
    re = lst[place]
    l = len(lst)
    lst[place]=0
    pl = (place+1)%l
    while re > 0:
        lst[pl] += 1
        pl = (pl + 1 )% l
        re-=1
    return lst


def part1(nums):
    used = []
    length = len(nums)
    counter = 1
    cont = True
    while cont:
        m = get_max_place(nums)
        nums = redistribute(nums, m)
        save = array_to_string(nums)
        if save in used:
            return counter
        counter+=1
        used.append(save)
    return get_max_place(nums)


def part2(nums):
    used = {}
    length = len(nums)
    counter = 1
    cont = True
    while cont:
        m = get_max_place(nums)
        nums = redistribute(nums, m)
        save = array_to_string(nums)
        if save in used:
            return counter-used[save]
        used[save]=counter
        counter+=1
    return get_max_place(nums)

print "part one answer"
print part1(get_input())
print "part two answer"
print part2(get_input())
