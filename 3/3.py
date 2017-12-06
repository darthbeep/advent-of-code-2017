import math

def ring(num):
    return [int(math.ceil(math.sqrt(num))/2), math.ceil(math.sqrt(num))]

def start(num):
    r = ring(num)[0]
    rs = ring(num)[1]-1
    #rstart = num - ((r+1) * (r+1))
    #print [rs, rstart]
    lasts = rs * rs
    rdist = num-lasts
    mdist = rdist % r

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
#print start(265149)

def fillGrid(num):
    x = 0
    y = 0
print start(265149)
#print math.sqrt(1024)
