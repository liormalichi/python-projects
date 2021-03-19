def HanoiTowers(start, via, target, n):
    if n>0:
        HanoiTowers(start, target, via, n-1)
        print("disk", n, "from", start, "to", target)
        HanoiTowers\
            (via, start, target, n-1)

HanoiTowers(1, 2 , 3, 3)
