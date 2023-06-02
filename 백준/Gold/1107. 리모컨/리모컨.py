import sys
input = sys.stdin.readline

t = int(input())
N = int(input())
broken_key = list(map(int, input().split()))
minimum = abs(100-t) 
for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j])in broken_key: #broken 키 값 탐색
            break
        elif j == len(i) -1:
            minimum = min(minimum, abs(int(i)-t)+len(i))
print(minimum)