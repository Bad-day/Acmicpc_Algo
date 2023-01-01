import sys; input=sys.stdin.readline;r=[];N = int(input())
for _ in range(N):
    r += list(map(int, input().split()));r = sorted(r, reverse=True)[:N];print(r[-1])
'''
for _ in range(N-1):
    num.remove(max(num));
print(max(num))
'''
#https://my-coding-notes.tistory.com/556
