import sys; input=sys.stdin.readline
n = int(input());a = set(map(int, input().split()))
m = int(input());arr = list(map(int, input().split()))
for i in arr:
	print(1) if i in a else print(0)
