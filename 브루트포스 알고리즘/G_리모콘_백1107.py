#brute force 알고리즘 방식 -> 모든 경우의수 탐색 
# 0 to 9 + - default - 100 
import sys
input = sys.stdin.readline

t = int(input())
N = int(input())
broken_key = list(map(int, input().split()))

minimum = abs(100-t) # 최솟값 default에서 + -만 사용하여 이동
for i in range(1000001):# 
    i = str(i)
    for j in range(len(i)):
        if int(i[j])in broken_key: #broken 키 값 
            break
        elif j == len(i) -1:
            minimum = min(minimum, abs(int(i)-t)+len(i))
print(minimum)