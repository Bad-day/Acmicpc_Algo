import sys; input=sys.stdin.readline
a,b = map(int, input().split());m=[]
for i in range(1,b+1):
    for j in range(i):
        m.append(i)
print(sum(m[a - 1:b]))