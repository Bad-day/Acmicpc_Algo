import sys; input=sys.stdin.readline
m, n = map(int, input().split());poknamedick={};pokiddick={}
for i in range(1, m+1):
    k = input().strip();pokiddick[i] = k;poknamedick[k]=i
for i in range(n):
    pok = input().strip()
    if pok.isalpha():
        print(poknamedick[pok])
    else:
        print(pokiddick[int(pok)])