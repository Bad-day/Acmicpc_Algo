# 0이나오면 종료시키는 간단한문제제
import sys; input=sys.stdin.readline
while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        break
    print(A+B)
    