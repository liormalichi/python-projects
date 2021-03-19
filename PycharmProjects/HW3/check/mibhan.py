def hemingway_encode(x3, x5, x6, x7):
    x1 = ( x3 + x5 + x7 ) % 2
    x2 = ( x3 + x6 + x7 ) % 2
    x4 = ( x5 + x6 + x7 ) % 2
    x8 = (x1+x2+x3+x4+x5+x6+x7) %2
    return (x1,x2,x3,x4,x5,x6,x7,x8)

def hamming_distance (s1 , s2 ):
    print(s1)
    print(s2)
    assert len ( s1 ) == len( s2 )
    return sum ( s1 [i ] != s2 [i] for i in range ( len ( s1 )))


def find_d_min():
    d = 8
    t = [(0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 0, 0), (1, 0, 0, 1),(1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]
    for i in range(15):
        s2 = hemingway_encode(t[i])
        new_hamming = hamming_distance(s2,(0,0,0,0,0,0,0,0))
        if new_hamming < d:
            d = new_hamming
    return d

    t = [(0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0,1,1,1)(1, 0, 0, 0), (1, 0, 0, 1),(1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]
import math
math.t
def find_d_min2():
    d = 8
    t = []
    s2 = hemingway_encode(1, 1, 0, 1)
    new_hamming = hamming_distance(s2,(0,0,0,0,0,0,0,0))
    if new_hamming < d:
        d = new_hamming
    return d

print(find_d_min2())

t= [(0,0,0,1),(0,0,1,0),(0,0,1,1),(0,1,0,0),(0,1,0,1),(0,1,1,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),(1,1,0,0),(1,1,0,1),(1,1,0,1),(1,1,1,0),(1,1,1,1)]
