import sys; input=sys.stdin.readline
a,b = map(int, input().split())
k = list(map(int, input().split()))
r = sorted(k, reverse=True)
print(r[b-1])