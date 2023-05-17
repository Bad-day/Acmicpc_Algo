import sys; input=sys.stdin.readline
nodick = []
n = int(input())
for _ in range(n):
        nodick.append(list(map(int, input().split())))
nodick.sort()
for i,j in nodick:
        print(i,j)