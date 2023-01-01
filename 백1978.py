import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
for i in num:
    if i == 1:
        N -=1
    for j in range(2,i):
        if i %j == 0:
            N -=1
            break
print(N)
