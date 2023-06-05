import sys; input=sys.stdin.readline;r=[];N = int(input())
for _ in range(N):
    r += list(map(int, input().split()));r = sorted(r, reverse=True)[:N];
print(r[-1])