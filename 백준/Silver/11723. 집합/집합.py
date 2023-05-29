import sys; input=sys.stdin.readline
m = int(input());s=set()
for _ in range(m):
    recent =input().strip().split()
    if len(recent) == 1:
        if recent[0] == "empty":
            s=set()
        else:
            s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        o, x = recent[0], recent[1];x=int(x)
        if  o == "add":
            s.add(x)
        elif o == "remove":
            s.discard(x)
        elif o == "check":
            print(1 if x in s else 0)
        elif o == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)