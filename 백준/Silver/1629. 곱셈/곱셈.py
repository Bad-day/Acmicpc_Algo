import sys;input=sys.stdin.readline
A,B,C = map(int, input().split())
def square(x,n,mod):
    if n == 1:
        return x%mod
    else:
        c = square(x,n//2,mod)
        if n %2==0:
            return (c*c) %mod
        else:
            return (c*c*x )%mod

print(square(A,B,C))