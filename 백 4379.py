import sys; input = sys.stdin.readline
t,a,b = map(int, input().split())
result = float(((t**a-1)/(t**b-1)));print(result)