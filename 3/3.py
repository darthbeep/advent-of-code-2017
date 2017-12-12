import math

def ring_num(num):
    return [int(math.ceil(math.sqrt(num))/2), math.ceil(math.sqrt(num))]

def solve_part1_with_math(num):
    r = ring_num(num)[0]
    square = (1+((r-1)*2)) ** 2
    s1 = square + r
    s2 = square + (r*3)
    s3 = square + (r*5)
    s4 = square + (r*7)
    close = [s1, s2, s3, s4]
    closest = num
    for thing in close:
        closest = min(closest, abs(num-thing))
    return closest+r

print solve_part1_with_math(265149)
