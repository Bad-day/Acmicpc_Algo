import sys; input=sys.stdin.readline
while True:
        n = list(map(int, input().split()))
        if sum(n) == 0:
                break
        mn = max(n);n.remove(mn)
        if n[0]**2 + n[1]**2 == mn**2:
                print('right')
        else:
                print('wrong')

