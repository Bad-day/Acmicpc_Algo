import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

def power(x, n, mod):
    if n == 1:
        return x % mod
    else:
        c = power(x, n // 2, mod) % mod
        if n % 2 == 0:
            return (c * c) % mod
        else:
            return (c * c * x) % mod

print(power(A, B, C))