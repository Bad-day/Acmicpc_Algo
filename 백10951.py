#EOF 처리하는 문제
import sys; input=sys.stdin.readline
while True:
    try:
        A,B = map(int, input().split())
    except:
        break
    print(A+B)