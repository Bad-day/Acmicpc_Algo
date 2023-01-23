#Case #x: A + B = C
import sys; input=sys.stdin.readline;count=1
n=int(input())
for i in range(n):
    A,B = map(int, input().split())
    print(f'Case #{count}: {A+B}')
    count+=1